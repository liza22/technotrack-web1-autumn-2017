# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.http import Http404
from django.core.urlresolvers import resolve

from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from blog.models import Blog, Post


#
# def blog(request, blog_name):
#     return render(request, 'blog_posts.html', {'blog_name': blog_name})
from comment.models import Comment


class BlogListForm(forms.Form):

    order_by = forms.ChoiceField(choices=(
        ('title', 'Имя'),
        ('id', 'ID'),
        ('created_at', 'Дата создания'),
        ('updated_at', 'Дата изменения'),
    ), required=False)

    title = forms.CharField(required=False)

    author = forms.CharField(required=False)


class BlogList(ListView):
    template_name = "core/blogs_list.html"
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 3

    def get_queryset(self):

        q = super(BlogList, self).get_queryset()

        self.form = BlogListForm(self.request.GET)

        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['title']:
                q = q.filter(title__contains=self.form.cleaned_data['title'])
            if self.form.cleaned_data['author']:
                q = q.filter(author__username__contains=self.form.cleaned_data['author'])
        return q

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['filterForm'] = self.form
        context['curr_url'] = resolve(self.request.path).url_name
        return context


class PostWithComments(ListView, CreateView):
    template_name = "blog/post.html"
    model = Comment
    fields = ('text', )
    paginate_by = 4
    object = None

    def get_success_url(self):
        return reverse('blogs:particular_post', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.filter(id=self.kwargs['pk']).first()
        return super(PostWithComments, self).form_valid(form)

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(PostWithComments, self).get_context_data(**kwargs)
        post = Post.objects.filter(id=self.kwargs['pk']).first()
        if post is None:
            raise Http404()
        context['post'] = post
        return context


class PostInBlog(ListView):
    template_name = "blog/blog_posts.html"
    model = Post
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(blog__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(PostInBlog, self).get_context_data(**kwargs)
        blog = Blog.objects.filter(id=self.kwargs['pk']).first()
        if blog is None:
            raise Http404()
        context['blog'] = blog
        return context


class NewBlog(CreateView):

    template_name = 'blog/new_blog.html'
    model = Blog
    fields = ('title', 'description')

    def get_success_url(self):
        return reverse('blogs:particular_blog', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewBlog, self).form_valid(form)


class NewPost(CreateView):

    template_name = 'blog/new_post.html'
    model = Post
    fields = ('title', 'text')

    def get_success_url(self):
        return reverse('blogs:particular_post', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = Blog.objects.filter(id=self.kwargs['pk']).first()
        return super(NewPost, self).form_valid(form)


class PostUpdate(UpdateView):

    template_name = 'blog/edit_post.html'
    model = Post
    fields = 'title', 'text'

    def get_queryset(self):
        return super(PostUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('blogs:particular_post', kwargs={'pk': self.object.pk})


class BlogUpdate(UpdateView):
    template_name = 'blog/edit_blog.html'
    model = Blog
    fields = ('title', 'description')

    def get_queryset(self):
        return super(BlogUpdate, self).get_queryset()\
            .filter(author=self.request.user)

    def get_success_url(self):
        return reverse('blogs:particular_blog', kwargs={'pk': self.object.pk})

