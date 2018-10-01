# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    location = models.TextField()
    bio = models.TextField()
    avatar = models.ImageField()
