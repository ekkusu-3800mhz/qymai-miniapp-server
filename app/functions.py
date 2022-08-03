from typing import Dict
from django.http import HttpResponse
import json


def response(status: int, data: Dict) -> HttpResponse:
    if data:
        res = {
            "status": status,
            "data": data,
        }
    else:
        res = {
            "status": status,
        }
    return HttpResponse(json.dumps(res))
