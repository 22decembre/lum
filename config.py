# -*- coding: utf-8 -*-

import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
LANG = 'fr'

#ldap auth
LDAP_HOST = 'blackblock.22decembre.eu'
DOMAIN = '22decembre.eu'
LDAP_BASE = 'dc=22decembre,dc=eu'
LDAP_GROUPS = 'ou=groups'
LDAP_USERS  = 'ou=users'
LDAP_ID = 'uid'
