# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def blogList(request):
    return render(request, 'blogs_list.html')
    
def blog(request, blog_name):
    return render(request, 'blog_posts.html', {'blog_name':blog_name})
    
def post(request, blog_name, post_id):
    return render(request, 'post.html', {'blog_name':blog_name, 'post_id':post_id})
   
def profile(request, person_name):
    return render(request, 'profile.html', {'person_name':person_name})
