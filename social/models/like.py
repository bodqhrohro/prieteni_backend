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

    class Meta:
        unique_together = ('post', 'user')

    def set_like(self, post, user):
        self.create(post=post, user=user)

    def unlike(self, post, user):
        self.objects.filter(post=post, user=user).delete()
