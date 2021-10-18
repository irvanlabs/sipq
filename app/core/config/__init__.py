import os

APP_NAME = os.getenv('APP_NAME') or 'SipQ'
VERSION = os.getenv('VERSION') or 'v0.0.1'
DEBUG = not not os.getenv('DEBUG')
