#coding: utf-8
from bson import ObjectId
from mongokit import Document, Connection

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

@conn.register
class Project(Document):
    __colection__ = project_coll.name
    structure = {
        'name': str,
        'desc': str,
        'owner': ObjectId,
        'start_date': {
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
        "media": str,
        "media_desc": str,
        "media_title": str,
        "start_date": {
            "year": int,
            "month": int,
            "day": int
        },
        "end_date": {
            "year": int,
            "month": int,
            "day": int
        },
    }


