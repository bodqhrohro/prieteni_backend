# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.hashers import make_password

from social.models import User


def hash_passwords(apps, schema_editor):
    users = User.objects.all()
    for user in users:
        # don't hash non-set passwords
        if user.password:
            user.password = make_password(user.password)
            user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20181003_1333'),
    ]

    operations = [
        migrations.RunPython(hash_passwords),
    ]
