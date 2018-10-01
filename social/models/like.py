# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Like(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
