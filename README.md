A simple backend for a social networking site in Python/Django.

Installation
============
```
virtualenv -p python2.7 --no-site-packages .env
. .env/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

API description
===============
```
GET /posts/ # list of posts
POST /posts/ # create a post
GET /posts/<id>/ # show the post
PUT /posts/<id>/ # edit the post
DELETE /posts/<id>/ # delete the post

GET /posts/<id>/likes # list of post likes
POST /posts/<id>/like # like the post
DELETE /posts/<id>/like # unlike the post

GET /users/ # list of users
POST /users/ # create a user
GET /users/<id>/ # show the user
PUT /users/<id>/ # edit the user
DELETE /users/<id>/ # delete the user

POST /api-token-auth/ # log in and obtain a JWT token
```

Post fields:
* id
* title
* body
* owner (read-only)
* liked_by_me (read-only)
* likes_count (read-only)

User fields:
* id
* name
* email
* password (write-only)
* location
* bio
* avatar

API-Token-Auth fields:
* username (email only, as names are allowed to conflict)
* password
