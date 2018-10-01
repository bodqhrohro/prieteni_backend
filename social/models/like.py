# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Like:
    post = models.ManyToManyField(
        'Post',
        on_delete=models.CASCADE,
    )
    user = models.ManyToManyField(
        'User',
        on_delete=models.CASCADE,
    )
