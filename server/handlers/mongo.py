#coding: utf-8
from bson import ObjectId
from mongokit import Document, Connection
from hashlib import md5

conn = Connection()
db = conn.timeline
user_coll = db['user']
project_coll = db['project']
card_coll = db['card']

class BaseDocument(Document):
    __database__ = db.name
    use_dot_notation = True

    def before_save(self):
        pass

    def save(self, uuid=False, validate=None, safe=True, *args, **kwargs):
        self.before_save()
        super(BaseDocument, self).save(uuid, validate, safe, *args, **kwargs)

@conn.register
class User(BaseDocument):
    __collection__ = user_coll.name
    structure = {
        'name': str,
        'password_hash': str,
        'role': str,
    }

    default_values = {
        'role': 'user'
    }

    @classmethod
    def hash_password(cls, password, name):
        password_with_salt = "{}-{}-{}".format(password, 'tlwj906', name)
        password_hash = md5(password_with_salt.encode()).hexdigest()
        return password_hash

@conn.register
class Project(Document):
    __collection__ = project_coll.name
    structure = {
        'url': str,
        'name': str,
        'desc': str,
        'owner': ObjectId,
        'start': {
            'year': int,
            'month': int,
            'day': int
        }
    }

@conn.register
class Card(BaseDocument):
    __collection__ = card_coll.name
    structure = {
        "project_id": ObjectId,
        "title": str,
        "desc": str,

        "media": {
            "src": str,
            "desc": str,
            "title": str,
        },

        "start": {
            "year": int,
            "month": int,
            "day": int
        },

        "end": {
            "year": int,
            "month": int,
            "day": int
        },
    }

    default_values = {
        'start.month': 0,
        'start.day': 0,
        'end.month': 0,
        'end.day': 0
    }

