import os, locale
'''
set bahasa ke indonesia id linux
edit file /etc/locale.gen dan uncomment
~$ sudo nano /etc/locale.gen
bagian id_ID.UTF-8. lalu jalankan command
~$ sudo locale-gen
'''
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

APP_NAME = os.getenv('APP_NAME') or 'SipQ'
VERSION = os.getenv('VERSION') or 'v0.0.1'
DEBUG = not not os.getenv('DEBUG')
SECRET = os.getenv('SECRET') or os.urandom(32)
API_PREFIX = '/api/v1'
