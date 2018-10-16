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

    def __str__(self):
        return '%s liked %s' % (self.user, self.post)

    @staticmethod
    def set_like(post, user):
        return Like.objects.create(post=post, user=user)

    @staticmethod
    def unlike(post, user):
        Like.objects.filter(post=post, user=user).delete()
