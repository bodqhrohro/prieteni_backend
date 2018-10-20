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

users = []


def check_result(response, success_message):
    if response.ok:
        print(success_message)
    else:
        print(response.text)


def generate_users(count):
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


script_directory = os.path.dirname(os.path.abspath(__file__))

ENDPOINT = sys.argv[1]
if not ENDPOINT.endswith('/'):
    ENDPOINT += '/'

with open(script_directory + '/config.json', 'r') as config_file:
    config = json.load(config_file)

    generate_users(config['number_of_users'])
