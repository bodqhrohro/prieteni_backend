# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserManager(models.Manager):
    def get_by_natural_key(self, key):
        return self.get(name=key)


class User(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    location = models.TextField(default='')
    bio = models.TextField(default='')
    avatar = models.ImageField(null=True, blank=True)

    objects = UserManager()

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def __str__(self):
        return '%s <%s>' % (self.name, self.email)
