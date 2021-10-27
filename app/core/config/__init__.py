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

DB_USER = os.getenv('DB_USER') or 'beb3a2595aa485'
DB_PASS = os.getenv('DB_PASS') or '3396d128'
DB_HOST = os.getenv('DB_HOST') or 'us-cdbr-east-04.cleardb.com'
DB_NAME = os.getenv('DB_NAME') or 'heroku_8fdf79d25619504'

MAX_DB_POOL_SIZE = 10

# DB_USER = os.getenv('DB_USER') or 'user'
# DB_PASS = os.getenv('DB_PASS') or 'user'
# DB_HOST = os.getenv('DB_HOST') or 'localhost'
# DB_NAME = os.getenv('DB_NAME') or 'user'
