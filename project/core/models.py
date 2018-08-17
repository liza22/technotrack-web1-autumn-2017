# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from blog.models import Blog


class User(AbstractUser):

    name = models.CharField(max_length=255, unique=False)
    username = models.CharField(max_length=255, unique=True)
