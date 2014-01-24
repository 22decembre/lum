# -*- coding: utf-8 -*-

import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
LANG = 'fr'

#ldap auth
LDAP_HOST = 'blackblock.22decembre.eu'
LDAP_DOMAIN = '22decembre.eu'
LDAP_BASE_DN = 'ou=users,dc=22decembre,dc=eu'
LDAP_ID = 'uid'
