#coding: utf-8
from datetime import timedelta

SERVER_HOST = 'lishi.me'
COOKIE_SECRET = 'tld913809yrasdkgnaoky0riasdhgjsgkjdabrb'
SENTRY_DSN = ( 'http://59bd31241c1a4629b4c6172a49c330a0:'
               '57c2aad3058b4307912a7aa1001d445f@sentry.weiju.net:10019/8')
DEBUG = False

TZ_OFFSET = timedelta(hours=8)  # local_time = utc_time + TZ_OFFSET


