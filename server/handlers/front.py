#coding: utf-8
import json
from bson import ObjectId

from .base import BaseRequestHandler
from .mongo import db

class IndexHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class ContentHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        result = {
            "timeline":
            {
                "headline":"中华五千年",
                "type":"default",
                "text":"粗略史",
                "startDate":"2012,1,26",
                "date": [
                    {
                        "startDate":"-4000",
                        "endDate":"-3000",
                        "headline":"三皇",
                        "text":"<p>中国传说中最早的年代</p>",
                        "asset":
                        {
                            "media":"/static/img/xizhou.jpg",
                            "credit":"燧人氏、伏羲氏、神农氏 都是些传说中的人物",
                            "caption":"非信史,就让他们流淌在传说中吧"
                        }
                    },
                    {
                        "startDate":"-3000",
                        "endDate":"-2029",
                        "headline":"五帝时代",
                        "text":"<p>稍微靠谱一点的传说中的时代, 都城在 有熊 平阳 蒲阪，今河南新郑 山西临汾 山西永济（一说在河北逐鹿) </p>",
                        "asset":
                        {
                            "media":"/static/img/xizhou.jpg",
                            "credit":"黄帝、颛顼、帝喾、尧、舜",
                            "caption":"非信史,就让他们流淌在传说中吧"
                        }
                    },
                    {
                        "startDate":"-3000",
                        "endDate":"-2029",
                        "headline":"五帝时代",
                        "text":"<p>稍微靠谱一点的传说中的时代, 都城在 有熊 平阳 蒲阪，今河南新郑 山西临汾 山西永济（一说在河北逐鹿) </p>",
                        "asset":
                        {
                            "media":"/static/img/xizhou.jpg",
                            "credit":"黄帝、颛顼、帝喾、尧、舜",
                            "caption":"非信史,就让他们流淌在传说中吧"
                        }
                    },
                    {
                        "startDate":"-1046",
                        "endDate":"-771",
                        "headline":"西周",
                        "text":"<p>周武王姬发创立于镐京</p>",
                        "asset":
                        {
                            "media":"/static/img/xizhou.jpg",
                            "credit":"国人暴动、共和行政",
                            "caption":"第一个信史"
                        }
                    },

                ]
            }
        }
        # self.respond_json(result)
        self.write(json.dumps(result))


class Project(BaseRequestHandler):
    def get(self, *args, **kwargs):
        url = kwargs.get('url')
        project = db.Project.find_one({"url": url})
        if project:
            self.render('project.html', project=project)
        else:
            self.render('index.html')


class ProjectInfo(BaseRequestHandler):
    def get(self, *args, **kwargs):
        project_id = ObjectId(self.get_argument('project_id'))
        project = db.Project.find_one(project_id)
        cards = db.Card.find({"project_id": project_id})
        ret_json = {
            "timeline":
            {
                "headline": project.title,
                "type": "default",
                "text": project.desc,
                "startDate": self.render_date(project.start),
                "date": []
            }
        }
        card_list = []
        for card in cards:
            card_list.append({
                "startDate": self.render_date(card.start),
                "endDate": self.render_date(card.end),
                "headline": card.title,
                "text": card.desc,
                "asset":
                {
                    "media": card.media.src,
                    "credit": card.media.desc,
                    "caption": card.media.title
                }
            })
        ret_json['timeline']['date'] = card_list
        self.respond_json(ret_json)

