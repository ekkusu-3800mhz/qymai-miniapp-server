from typing import Dict
import json


def makeResponse(status: int, data: Dict) -> str:
    res = {
        "status": status,
        "data": data,
    }
    return json.dumps(res)
