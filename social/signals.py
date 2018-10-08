# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.hashers import make_password

from .models import User


@receiver(pre_save, sender=User)
def password_hasher(instance, **kwargs):
    instance.password = make_password(instance.password)
