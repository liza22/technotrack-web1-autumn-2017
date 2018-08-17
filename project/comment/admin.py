# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from blog.models import Post
from comment.models import Comment


class CommentsInline(admin.TabularInline):

    model = Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = 'id', 'text',


