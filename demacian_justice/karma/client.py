import requests, os
from django.conf import settings

class Client:
    HEADERS = {'X-Riot-Token': settings.RIOT_API_KEY}
    HOST_NAME = ".api.riotgames.com"
    SUMMONER_ENDPOINT = "/lol/summoner/v4/summoners/by-name/"

    # curl -X GET 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'
    def get_summoner(self, summoner_name, server):
        url = "https://" + server + Client.HOST_NAME + Client.SUMMONER_ENDPOINT + summoner_name
        response = requests.get(url = url, headers = Client.HEADERS)
        return response
