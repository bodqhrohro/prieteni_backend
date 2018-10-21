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


def obtain_tokens(users):
    tokens = []

    for email, password in users:
        result = requests.post(ENDPOINT + 'api-token-auth/', data={
            'username': email,
            'password': password,
        })
        result = check_result(result, 'Authenticated as ' + email)
        if result:
            tokens.append(result.json()['token'])

    return tokens


def generate_posts(count, token):
    posts = []

    for i in range(count):
        title = fake.title()
        body = fake.text()

        result = requests.post(ENDPOINT + 'posts/', data={
            'title': title,
            'body': body,
        }, headers={
            'Authorization': 'JWT ' + token,
        })
        result = check_result(result, 'Created post "%s"' % title)
        if result:
            posts.append(result.json()['id'])

    return posts


script_directory = os.path.dirname(os.path.abspath(__file__))

ENDPOINT = sys.argv[1]
if not ENDPOINT.endswith('/'):
    ENDPOINT += '/'

with open(script_directory + '/config.json', 'r') as config_file:
    config = json.load(config_file)

    users = generate_users(config['number_of_users'])
    tokens = obtain_tokens(users)

    posts = []
    for token in tokens:
        posts += generate_posts(random.randint(1, config['max_posts_per_user']),
                               token)
