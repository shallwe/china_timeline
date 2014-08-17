#coding: utf-8
import json

from .base import BaseRequestHandler

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