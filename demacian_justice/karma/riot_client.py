import requests, os
from django.conf import settings

class RiotClient:
    HEADERS = {'X-Riot-Token': settings.RIOT_API_KEY}
    HOST_NAME = ".api.riotgames.com"
    SUMMONER_ENDPOINT = "/lol/summoner/v4/summoners/by-name/"

    # curl -X GET 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'
    def get_summoner(self, summoner_name, server):
        url = "https://" + server + RiotClient.HOST_NAME + RiotClient.SUMMONER_ENDPOINT + summoner_name
        response = requests.get(url = url, headers = RiotClient.HEADERS)
        return response
