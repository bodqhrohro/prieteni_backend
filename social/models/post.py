# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.TextField()
    body = models.TextField()
    owner = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
