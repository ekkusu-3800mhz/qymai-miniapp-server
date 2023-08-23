from django.views import View
from django.http import HttpRequest, HttpResponse
from app.settings import DEBUG
from app.functions import response
from app.models import Shop, Game, Cabinet


class InitData(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        if DEBUG:
            # 注册游戏类型
            maimai = Game(name='舞萌DX 2022', alias='maimaidx_cn')
            chunithm = Game(name='中二节奏NEW', alias='chunithm_cn')
            maimai.save()
            chunithm.save()
            # 注册本地店铺
            n = Shop(name='疯狂牛仔城', address='广东省清远市清城区先锋东路39号世纪荟广场1F', fixedLocation='23.710194,113.037729', businessTime='工作日：10:00至22:00；假日：10:00至22:30')
            t = Shop(name='天空之城', address='广东省清远市清城区湖西路89号万达广场3F-A-1号商铺', fixedLocation='23.713615,113.013418', businessTime='10:00至22:30')
            j = Shop(name='极限主场', address='广东省清远市清城区先锋中路18号城市广场3F', fixedLocation='23.708096,113.030317', businessTime='工作日：10:00至23:00；假日：09:30至23:30')
            d = Shop(name='欢乐时光', address='广东省清远市清城区东湖路汇利安广场壹号3F商铺306-308号', fixedLocation='23.709692,113.035828', businessTime='工作日：10:00至22:00；假日：10:00至22:30')
            n.save()
            t.save()
            j.save()
            d.save()
            # 注册 maimai 机台信息
            Cabinet(shop=n, game=maimai, version='CN1.30-D', credit=5, number=1, enablePlayerCount=True, maxCapacity=8, name='牛仔城直播机', uniqueName="牛舞萌右机").save()
            Cabinet(shop=n, game=maimai, version='CN1.30-D', credit=5, number=1, enablePlayerCount=True, maxCapacity=8, name="牛仔城非直播机", uniqueName="牛舞萌左机").save()
            Cabinet(shop=t, game=maimai, version='CN1.30-D', credit=3, number=1, enablePlayerCount=True, maxCapacity=8, name="天空之城", uniqueName="万达").save()
            Cabinet(shop=j, game=maimai, version='CN1.30-D', credit=4, number=1, enablePlayerCount=True, maxCapacity=8, name="极限主场", uniqueName="城广").save()
            Cabinet(shop=d, game=maimai, version='CN1.30-D', credit=4, number=1, enablePlayerCount=True, maxCapacity=8, name="欢乐时光", uniqueName="大润发").save()
            # 注册 chunithm 机台信息
            Cabinet(shop=n, game=chunithm, version='CN1.01-2023/07/28', credit=5, number=1, enablePlayerCount=True, maxCapacity=8, name='牛仔城左机', uniqueName='牛中二左机').save()
            Cabinet(shop=n, game=chunithm, version='CN1.01-2023/07/28', credit=5, number=1, enablePlayerCount=True, maxCapacity=8, name='牛仔城右机', uniqueName='牛中二右机').save()
            return response(status=200, data={})
        return response(status=403, data={})
