from django.views import View
from django.http import HttpRequest, HttpResponse
from app.settings import DEBUG
from app.functions import response
from app.models import Shop, Cabinet


class InitDataView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        if DEBUG:
            n = Shop(name='疯狂牛仔城', address='广东省清远市清城区先锋东路39号世纪荟广场一层', fixedLocation='23.710194,113.037729')
            t = Shop(name='天空之城', address='广东省清远市清城区湖西路89号万达广场3F-A-1号商铺', fixedLocation='23.713615,113.013418')
            j = Shop(name='极限主场', address='广东省清远市清城区先锋中路18号城市广场三楼', fixedLocation='23.708096,113.030317')
            d = Shop(name='欢乐时光', address='广东省清远市清城区东湖路汇利安广场壹号3层商铺306-308号', fixedLocation='23.709692,113.035828')
            n.save()
            t.save()
            j.save()
            d.save()
            Cabinet(shop=n, version='CH1.20-A', credit=5, number=1, enablePlayerCount=True, maxCapacity=8).save()
            Cabinet(shop=t, version='CH1.20-A', credit=0, number=1, enablePlayerCount=True, maxCapacity=8).save()
            Cabinet(shop=j, version='CH1.20-A', credit=4, number=1, enablePlayerCount=True, maxCapacity=8).save()
            Cabinet(shop=d, version='CH1.20-A', credit=4, number=1, enablePlayerCount=True, maxCapacity=8).save()
            return response(status=200, data={})
        return response(status=403, data={})
