import requests, os
from django.conf import settings

class Client:
    URL = "https://euw1.api.riotgames.com"
    HEADERS = {'X-Riot-Token': settings.RIOT_API_KEY}

    # curl -X GET 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'
    def get_summoner(self, summoner_name):
        endpoint = "/lol/summoner/v4/summoners/by-name/" + summoner_name
        response = requests.get(url = Client.URL + endpoint, headers = Client.HEADERS)
        return response
