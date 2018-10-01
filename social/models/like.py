# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .post import Post
from .user import User


class Like(models.Model):
    post = models.ManyToManyField(Post)
    user = models.ManyToManyField(User)
