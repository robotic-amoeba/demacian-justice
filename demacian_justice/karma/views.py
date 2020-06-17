from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime, date

from .riot_client import RiotClient
from .models import Summoner
from karma.utils.karma_compute import *

import json

def index(request):
    return HttpResponse("You're at the karma index.")

def get_summoner(request):
    riot_response = __riot_request(request)
    return __enriched_riot_response(riot_response)

@csrf_exempt
def vote(request):
    body = json.loads(request.body)
    summoner, _ = Summoner.objects.get_or_create(puuid = body['summoner_uuid'])
    updated_summoner = summoner.vote(body['vote'])
    processed_summoner = __processed_summoner(updated_summoner)
    return JsonResponse(processed_summoner, status=200)

def __riot_request(request):
    server = request.GET.get('server')
    summoner_name = request.GET.get('name')
    riot_client = RiotClient()
    response = riot_client.get_summoner(summoner_name, server)
    settings.LOGGER.info('Riot response[' + str(response.status_code) + ']:' + response.content.decode('utf-8'))
    return response

def __enriched_riot_response(riot_response):
    riot_body = riot_response.json()
    if riot_response.status_code >= 400:
        return JsonResponse(riot_body, status=riot_response.status_code)

    puuid = riot_body['puuid']
    riot_body.update(__summoner_info(puuid))
    return JsonResponse(riot_body, status=riot_response.status_code)

def __summoner_info(puuid):
    summoner = Summoner.objects.filter(puuid=puuid)
    if len(summoner) == 0:
        return {'karma': 0, 'upvotes': 0, 'downvotes': 0 }

    dict_summoner = model_to_dict(summoner.first())
    __add_karma(dict_summoner)
    return dict_summoner

def __processed_summoner(summoner_model):
    dict_summoner = __date_remover(model_to_dict(summoner_model))
    __add_karma(dict_summoner)
    return dict_summoner

def __add_karma(dict_summoner):
    wilson_value = wilson_score(dict_summoner['upvotes'], dict_summoner['downvotes'])
    karma =  int(wilson_value * 100)
    dict_summoner.update({ 'karma': karma })

def __date_remover(dict):
    purged_dict =  dict.copy()
    for key in dict:
        if isinstance(dict[key], (datetime, date)):
            purged_dict.pop(key)
    return purged_dict
