# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    location = models.TextField(default='')
    bio = models.TextField(default='')
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '%s <%s>' % (self.name, self.email)
