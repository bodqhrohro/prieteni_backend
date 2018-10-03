# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.TextField(default='')
    body = models.TextField(default='')
    owner = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
