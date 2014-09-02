#coding: utf-8
from bson import ObjectId

from .base import BaseAdminHandler, BaseRequestHandler
from .mongo import db, User

class LoginHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.render('hote/login.html')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        password = self.get_argument('password')

        if name:
            name = name.lower()

        user = db.User.find_one({"name": name})
        if not user:
            return self.respond_json({
                'error': 'NAME',
                'message': u'该用户名不存在'
            })

        password_hash = User.hash_password(password)
        if user.password_hash != password_hash:
            return self.respond_json({
                'error': 'PASSWORD',
                'message': u'密码错误，请重新输入'
            })

        self.set_secure_cookie('_id', str(user._id))
        return self.redirect('/hote')


class RegisterHandler(BaseRequestHandler):
    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        password = self.get_argument('password')

        if name:
            name = name.lower()

        user = db.User.find_one({"name": name})
        if user:
            return self.finish('该用户名已存在')

        user = db.User()
        user.name = name
        user.password_hash = User.hash_password(password, name)
        user.save()
        self.set_secure_cookie('_id', str(user._id))
        return self.redirect('/hote')

class LogoutHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.set_secure_cookie('_id', '', -1)
        self.redirect('/hote/login')


class IndexHandler(BaseAdminHandler):
    def get(self, *args, **kwargs):
        self.render('hote/index.html', user=self.current_user)


class ListProject(BaseAdminHandler):
    def get(self, *args, **kwargs):
        projects = list(db.Project.find({"owner": self.current_user._id}))
        for project in projects:
            project['card_num'] = db.Card.find({"project_id": project._id}).count()
        self.respond_json({"projects": projects})


class ProjectInfo(BaseAdminHandler):
    def get(self, *args, **kwargs):
        url = kwargs.get('url')
        project = db.Project.find_one({"url": url})
        return self.render('hote/project.html', project=project, user=self.current_user)

class AddProject(BaseAdminHandler):
    def post(self, *args, **kwargs):
        project = db.Project()
        project.url = self.get_argument('url')
        project.name = self.get_argument('name')
        project.desc = self.get_argument('desc')
        project.owner = self.current_user._id
        project.start.year = int(self.get_argument('year'))
        project.start.month = int(self.get_argument('month', 0))
        project.start.day = int(self.get_argument('day', 0))
        project.save()
        self.respond_json(project)


class ListCard(BaseAdminHandler):
    def get(self, *args, **kwargs):
        project_id = self.get_argument('project_id')
        cards = list(db.Card.find({"project_id": ObjectId(project_id)}))
        self.render('hote/cards.html', cards=cards)


class AddCard(BaseAdminHandler):
    def post(self, *args, **kwargs):
        card = db.Card()
        card.project_id = ObjectId(self.get_argument('project_id'))
        card.title = self.get_argument('title')
        card.desc = self.get_argument('desc')
        card.media.src = self.get_argument('media_src')
        card.media.title = self.get_argument('media_title')
        card.media.desc= self.get_argument('media_desc')
        card.start.year = int(self.get_argument('start_year'))
        card.start.month = int(self.get_argument('start_month', 0))
        card.start.day = int(self.get_argument('start_day', 0))
        card.end.year = int(self.get_argument('end_year'))
        card.end.month = int(self.get_argument('end_month', 0))
        card.end.day = int(self.get_argument('end_day', 0))
        card.save()
        self.respond_json(card)



