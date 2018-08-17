# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blog.models import Blog, Post
from comment.admin import CommentsInline


class PostsInline(admin.TabularInline):

    model = Post


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = 'id', 'title', 'description'
    list_editable = 'title', 'description'
    inlines = PostsInline,


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = 'id', 'title',
    inlines = CommentsInline,
