#coding: utf-8

from datetime import datetime
import json
import logging
import time

from bson import ObjectId
from tornado.web import RequestHandler
from raven.contrib.tornado import SentryMixin

from .mongo import db

logger = logging.getLogger('h.base')
logger.setLevel(logging.DEBUG)
FORMAT = '%(asctime)-15s %(name)-15s %(levelname)-5s: %(message)s'
logging.basicConfig(format=FORMAT)

ALIVE_DURATION = 60
EMIT_CALLBACK_TIMEOUT = 10


def jsonable(o):
    """ 将对象转化为能直接json_encode的对象
    """
    if isinstance(o, dict):
        d = {}
        for key in o:
            d[key] = jsonable(o[key])
        return d
    elif type(o) in [list, tuple, set]:
        li = []
        for i, item in enumerate(o):
            li.append(jsonable(item))
        return li
    elif type(o) == datetime:
        return time.mktime(o.timetuple())
    elif type(o) == ObjectId:
        return str(o)
    else:
        return o


class BaseRequestHandler(SentryMixin, RequestHandler):
    def respond_json(self, data):
        """ 返回json/jsonp的数据
         如果argument中带有callback参数，则返回jsonp的script，否则返回json数据
        """
        callback = self.get_argument('callback', None)
        json_str = json.dumps(jsonable(data))
        if callback:
            self.set_header('Content-Type', 'application/x-javascript;charset=UTF-8')
            self.write('%s(%s);' % (callback, json_str))
        else:
            self.set_header('Content-Type', 'application/json;charset=UTF-8')
            self.write(json_str)
        self.finish()

    def get_date_argument(self):
        date_string = self.get_argument('date', None)
        if not date_string:
            date = datetime(*datetime.now().timetuple()[:3])
        else:
            date = datetime.strptime(date_string, '%Y-%m-%d')
        return date

    def render_date(self, _date):
        ret_str = "{}".format(_date.year)
        if _date.month != 0:
            ret_str += ",{}".format(_date.month)
            if _date.day != 0:
                ret_str += ",{}".format(_date.day)
        return ret_str


class BaseAdminHandler(BaseRequestHandler):
    def prepare(self):
        _id = self.get_secure_cookie('_id')
        if _id:
            self.current_user = db.User.find_one(ObjectId(_id))
        else:
            self.redirect('/hote/login?callback=%s' % self.request.full_url())
