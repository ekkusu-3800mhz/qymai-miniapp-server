from typing import List
from django.utils import timezone
from django.views import View
from django.http import HttpRequest, HttpResponse
from app.functions import response
from app.models import Cabinet
from app.forms.queue import UpdatePlayerForm
import json


class CabinetList(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        cabs: List = list(Cabinet.objects.all())
        l: List = []
        for c in cabs:
            l.append({
                'id': c.id,
                'shop': {
                    'id': c.shop.id,
                    'name': c.shop.name,
                    'address': c.shop.address,
                    'location': c.shop.fixedLocation,
                },
                'game': c.game.name,
                'version': c.version,
                'number': c.number,
                'enablePlayerCount': c.enablePlayerCount,
                'playerCount': c.playerCount,
                'maxCapacity': c.maxCapacity,
                'updateTime': None if not c.playerCountUpdateTime else timezone.make_naive(c.playerCountUpdateTime).strftime('%Y-%m-%d %H:%M:%S'),
            })
        res = {
            'cabinetList': l,
        }
        return response(status=200, data=res)


class UpdatePlayer(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        form = UpdatePlayerForm(request.POST)
        if not form.is_valid():
            return response(status=400, data={"error": json.loads(form.errors.as_json())})
        data = form.cleaned_data
        if Cabinet.objects.filter(id=data['cabinet_id']):
            cabinet = Cabinet.objects.get(id=data['cabinet_id'])
            if cabinet.enablePlayerCount:
                if data['player_count'] <= 0:
                    cabinet.playerCount = 0
                else:
                    cabinet.playerCount = data['player_count']
            cabinet.playerCountUpdateTime = timezone.now()
            cabinet.save()
        return response(status=200, data={})
