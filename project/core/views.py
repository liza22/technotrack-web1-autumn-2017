# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import resolve
from django.views.generic import TemplateView
from blog.models import Post, Blog
from comment.models import Comment


def profile(request, person_name):
    return render(request, 'core/profile.html', {'person_name': person_name})


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('name', 'username')

        labels = {
            'name': 'Full name',
            'username': 'Username'
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.name = self.cleaned_data['name']
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password1']
        user.set_password(user.password)

        if commit:
            user.save()
        return user


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})


class HomePageView(TemplateView):

    template_name = "core/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['numPosts'] = Post.objects.all().count()
        context['numBlogs'] = Blog.objects.all().count()
        context['numComments'] = Comment.objects.all().count()
        context['curr_url'] = resolve(self.request.path).url_name
        return context
