from django.views import View
from django.http import HttpRequest, HttpResponse
from app.settings import DEBUG
from app.functions import response
from app.models import Shop, Game, Cabinet


class InitData(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        if DEBUG:
            game = Game(name='舞萌DX 2022', alias='maimaidx_cn')
            game.save()
            n = Shop(name='疯狂牛仔城', address='广东省清远市清城区先锋东路39号世纪荟广场一层', fixedLocation='23.710194,113.037729', businessTime='10:00至23:00')
            t = Shop(name='天空之城', address='广东省清远市清城区湖西路89号万达广场3F-A-1号商铺', fixedLocation='23.713615,113.013418', businessTime='10:00至22:30')
            j = Shop(name='极限主场', address='广东省清远市清城区先锋中路18号城市广场三楼', fixedLocation='23.708096,113.030317', businessTime='周一至周五：10:00至23:00；周六至周日：09:30至23:30')
            d = Shop(name='欢乐时光', address='广东省清远市清城区东湖路汇利安广场壹号3层商铺306-308号', fixedLocation='23.709692,113.035828', businessTime='周一至周五：10:00至22:00；周六至周日：10:00至22:30')
            n.save()
            t.save()
            j.save()
            d.save()
            Cabinet(shop=n, game=game, version='CH1.20-B', credit=5, number=1, enablePlayerCount=True, maxCapacity=8, remark='机况随着机台位置变更会有不同，若出现吃音请立即和店员联系').save()
            Cabinet(shop=t, game=game, version='CH1.20-B', credit=0, number=1, enablePlayerCount=True, maxCapacity=8, remark='左侧（1P）4号键震键，待修').save()
            Cabinet(shop=j, game=game, version='CH1.20-B', credit=4, number=1, enablePlayerCount=True, maxCapacity=8).save()
            Cabinet(shop=d, game=game, version='CH1.20-B', credit=4, number=1, enablePlayerCount=True, maxCapacity=8).save()
            return response(status=200, data={})
        return response(status=403, data={})
