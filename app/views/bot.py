from typing import List
from django.utils import timezone
from django.views import View
from django.http import HttpRequest, HttpResponse
from app.functions import response
from app.models import Game, Cabinet
from app.forms.bot import UpdatePlayerForm
import json


class MaimaiCabinetList(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        maimai = Game.objects.get(alias='maimaidx_cn')
        cabs: List = list(Cabinet.objects.filter(game=maimai))
        l: List = []
        for c in cabs:
            l.append({
                'name': c.name,
                'uniqueName': c.uniqueName,
                'number': c.number,
                'playerCount': c.playerCount,
                'maxCapacity': c.maxCapacity,
                'updateTime': None if not c.playerCountUpdateTime else timezone.make_naive(c.playerCountUpdateTime).strftime('%Y-%m-%d %H:%M:%S'),
            })
        res = {
            'error': None,
            'cabinetList': l,
        }
        return response(status=200, data=res)
    

class ChunithmCabinetList(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        chunithm = Game.objects.get(alias='chunithm_cn')
        cabs: List = list(Cabinet.objects.filter(game=chunithm))
        l: List = []
        for c in cabs:
            l.append({
                'name': c.name,
                'uniqueName': c.uniqueName,
                'number': c.number,
                'playerCount': c.playerCount,
                'maxCapacity': c.maxCapacity,
                'updateTime': None if not c.playerCountUpdateTime else timezone.make_naive(c.playerCountUpdateTime).strftime('%Y-%m-%d %H:%M:%S'),
            })
        res = {
            'error': None,
            'cabinetList': l,
        }
        return response(status=200, data=res)
    

class UpdatePlayer(View):

    def post(self, request: HttpRequest) -> HttpResponse:
        form = UpdatePlayerForm(request.POST)
        if not form.is_valid():
            return response(status=400, data={"error": json.loads(form.errors.as_json())})
        data = form.cleaned_data
        if data['player_count'] > 20:
            return response(status=403, data={"error": "单次加卡不可超过20张，若出现超过20人排队请分批添加。"})
        res = {
            'error': None,
        }
        if Cabinet.objects.filter(uniqueName=data['unique_name']):
            cabinet = Cabinet.objects.get(uniqueName=data['unique_name'])
            if data['player_count'] <= 0:
                cabinet.playerCount = 0
            else:
                cabinet.playerCount = data['player_count']
            cabinet.playerCountUpdateTime = timezone.now()
            cabinet.save()
            res = {
                'error': None,
                'cabinetInfo': {
                    'name': cabinet.name,
                    'uniqueName': cabinet.uniqueName,
                    'number': cabinet.number,
                    'playerCount': cabinet.playerCount,
                    'maxCapacity': cabinet.maxCapacity,
                    'updateTime': None if not cabinet.playerCountUpdateTime else timezone.make_naive(cabinet.playerCountUpdateTime).strftime('%Y-%m-%d %H:%M:%S'),
                },
            }
        return response(status=200, data=res)
