# -*- coding: utf-8 -*-

DEBUG = True,
SECRET_KEY = 'should always be secret',
# Database settings:

SQLALCHEMY_DATABASE_URI = 'sqlite:///guest_book.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = False
