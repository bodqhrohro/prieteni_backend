#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import os
import sys
import json
import random
import io

import fake
import pagan
import requests

ENDPOINT = ''


def check_result(response, success_message):
    if response.ok:
        print(success_message)
        return response
    else:
        print(response.text)
        return None


def generate_users(count):
    users = []

    for i in range(count):
        name = fake.name()
        email = fake.email()
        password = fake.name()
        location = ', '.join((fake.address(), fake.city(), fake.country()))
        bio = fake.text()
        avatar = pagan.Avatar(name)

        temp = io.BytesIO()
        avatar.img.save(temp, format='gif')

        users.append((email, password))
        result = requests.post(ENDPOINT + 'users/', data={
            'name': name,
            'email': email,
            'password': password,
            'location': location,
            'bio': bio,
        }, files={
            'avatar': ('image.gif', temp.getvalue()),
        })
        check_result(result, 'Created user ' + name)

    return users


def generate_posts(max_count, users):
    for email, password in users:
        result = requests.post(ENDPOINT + 'api-token-auth/', data={
            'username': email,
            'password': password,
        })
        result = check_result(result, 'Authenticated as ' + email)
        if result:
            token = result.json()['token']
            print(token)


script_directory = os.path.dirname(os.path.abspath(__file__))

ENDPOINT = sys.argv[1]
if not ENDPOINT.endswith('/'):
    ENDPOINT += '/'

with open(script_directory + '/config.json', 'r') as config_file:
    config = json.load(config_file)

    users = generate_users(config['number_of_users'])
    posts = generate_posts(config['max_posts_per_user'], users)
