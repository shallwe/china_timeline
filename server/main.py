#coding: utf-8

import os

from tornado import web, template
from jinja2 import Environment, FileSystemLoader
from raven.contrib.tornado import AsyncSentryClient
from tornado.web import StaticFileHandler

from .handlers import front, hote
from .settings import COOKIE_SECRET, SENTRY_DSN, DEBUG


PACKAGE_FOLDER = os.path.dirname(__file__)
TEMPLATE_FOLDER = 'templates'
ABS_TEMPLATE_FOLDER_PATH = os.path.join(PACKAGE_FOLDER, TEMPLATE_FOLDER)

env = Environment(loader=FileSystemLoader(ABS_TEMPLATE_FOLDER_PATH))


class Jinja2TemplateLoader(template.Loader):
    def _create_template(self, name):
        template = env.get_template(name)
        # 生成模板时，tornado会调用generate方法，但是在jinja2里面generate会生成一个generator（而不是string）
        template.generate = template.render
        return template


routes = [
    (r"/", front.IndexHandler),
    (r"/content", front.ContentHandler),
    (r"/project/(?P<url>.*?)", front.Project),
    (r"/project/info", front.ProjectInfo),

    (r"/hote/login", hote.LoginHandler),
    (r"/hote/logout", hote.LogoutHandler),
    (r"/hote/list_project", hote.ListProject),
    (r"/hote/add_project", hote.AddProject),
    (r"/hote/list_card", hote.ListCard),
    (r"/hote/add_card", hote.AddCard),

    (r"/templates/(.*?)", StaticFileHandler, dict(path=os.path.join(PACKAGE_FOLDER, 'templates'))),
]

application = web.Application(
    routes,
    template_loader=Jinja2TemplateLoader(ABS_TEMPLATE_FOLDER_PATH),
    static_path=os.path.join(PACKAGE_FOLDER, 'static'),
    cookie_secret=COOKIE_SECRET,
    debug=DEBUG,
)

application.sentry_client = AsyncSentryClient(SENTRY_DSN)