from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from .client import Client
from .models import Summoner

import json

def index(request):
    return HttpResponse("You're at the karma index.")
    # summoner_info = {'id': '0BIcOHrs5k6h6i0JFq3Z9YtBerh-HA5D4zAMjb3rPq4Rg34',
    #                      'accountId': '6c-2t4GjYiljgGoz-Rq6xsEPcupymkR8_kjWgamIxPUPag',
    #                      'puuid': 'VDfFDa_56cNgF1Jw54DuXoCO8edI7yVDaAiMe9vIyCOoKqXcDy-fvYB_iSIeiWa5gJxH5A4eVcp3yw',
    #                      'name': 'Kixmo',
    #                      'profileIconId': 4227,
    #                      'revisionDate': 1586719398000,
    #                      'summonerLevel': 195}
    # return JsonResponse(summoner_info)

def get_summoner(request):
    server = request.GET.get('server')
    summoner_name = request.GET.get('name')
    client = Client()
    response = client.get_summoner(summoner_name, server)
    settings.LOGGER.info('Riot response[' + str(response.status_code) + ']:' + response.content.decode('utf-8'))
    return JsonResponse(response.json(), status=response.status_code)

@csrf_exempt
def vote(request):
    body = json.loads(request.body)
    summoner, _ = Summoner.objects.get_or_create(puuid = body['summoner_uuid'])
    updated_summoner = summoner.vote(body['vote'])
    dict_summoner = model_to_dict(updated_summoner)
    serialized_summoner = json.dumps(dict_summoner, default=str)
    return JsonResponse(serialized_summoner, safe=False, status=200)

