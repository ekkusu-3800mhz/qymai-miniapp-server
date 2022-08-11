from typing import List
from django.utils import timezone
from django.views import View
from django.http import HttpRequest, HttpResponse
from app.functions import response
from app.models import Shop, Cabinet


class ShopList(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        shops: List = list(Shop.objects.all())
        l: List = []
        for s in shops:
            l.append({
                'id': s.id,
                'name': s.name,
                'address': s.address,
                'location': s.fixedLocation,
            })
        res = {
            'shopList': l,
        }
        return response(status=200, data=res)


class ShopInfo(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        id = request.GET.get('shop_id')
        if Shop.objects.filter(id=id):
            shop: Shop = Shop.objects.get(id=id)
            res = {
                'shopInfo': {
                    'id': shop.id,
                    'name': shop.name,
                    'address': shop.address,
                    'location': shop.fixedLocation,
                    'description': shop.description,
                    'creditPrice': shop.creditPrice,
                    'businessTime': shop.businessTime,
                    'remark': shop.remark,
                },
            }
            return response(status=200, data=res)
        return response(status=404, data={"error": "未找到相应的店铺条目"})


class CabinetInfo(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        id = request.GET.get('shop_id')
        if Shop.objects.filter(id=id):
            shop: Shop = Shop.objects.get(id=id)
            cabinets: List = list(Cabinet.objects.filter(shop=shop))
            l: List = []
            for c in cabinets:
                l.append({
                    'id': c.id,
                    'game': c.game.name,
                    'version': c.version,
                    'credit': c.credit,
                    'number': c.number,
                    'enablePlayerCount': c.enablePlayerCount,
                    'playerCount': c.playerCount,
                    'maxCapacity': c.maxCapacity,
                    'updateTime': None if not c.playerCountUpdateTime else timezone.make_naive(c.playerCountUpdateTime).strftime('%Y-%m-%d %H:%M:%S'),
                    'remark': c.remark,
                })
            res = {
                'shopInfo': {
                    'id': shop.id,
                    'name': shop.name,
                    'address': shop.address,
                    'location': shop.fixedLocation,
                    'description': shop.description,
                    'creditPrice': shop.creditPrice,
                    'businessTime': shop.businessTime,
                    'remark': shop.remark,
                },
                'cabinetList': l,
            }
            return response(status=200, data=res)
        return response(status=404, data={"error": "未找到相应的店铺条目"})
