from django.test import TestCase, Client
from nose.tools import assert_true
import httpretty
import json
import re


class SummonerAPITestCase(TestCase):
    RIOT_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/.*"

    @httpretty.activate
    def test_client_get_success(self):
        """GET request to client successes"""
        summoner_info = {'id': '0BIcOHrs5k6h6i0JFq3Z9YtBerh-HA5D4zAMjb3rPq4Rg34',
                         'accountId': '6c-2t4GjYiljgGoz-Rq6xsEPcupymkR8_kjWgamIxPUPag',
                         'puuid': 'VDfFDa_56cNgF1Jw54DuXoCO8edI7yVDaAiMe9vIyCOoKqXcDy-fvYB_iSIeiWa5gJxH5A4eVcp3yw',
                         'name': 'Kixmo',
                         'profileIconId': 4227,
                         'revisionDate': 1586719398000,
                         'summonerLevel': 195}

        httpretty.register_uri(httpretty.GET, re.compile(SummonerAPITestCase.RIOT_URL),
                               body=json.dumps(summoner_info))

        test_client = Client()
        response = test_client.get(
            '/karma/get_summoner', {'summoner_name': 'feeder_sticks'})

        self.assertEqual(json.loads(response.content), summoner_info)
        self.assertEqual(response.status_code, 200)

    @httpretty.activate
    def test_client_get_server_error(self):
        """GET request to client returns server error"""
        httpretty.register_uri(httpretty.GET, re.compile(SummonerAPITestCase.RIOT_URL),
                               status=500)

        test_client = Client()
        response = test_client.get(
            '/karma/get_summoner', {'summoner_name': 'feeder_sticks'})

        self.assertEqual(response.status_code, 500)

    @httpretty.activate
    def test_client_get_not_found(self):
        """GET request to client returns not found"""
        riot_answer = {"status":
                       {"message": "Data not found - summoner not found", "status_code": 404}}
        httpretty.register_uri(httpretty.GET, re.compile(SummonerAPITestCase.RIOT_URL),
                               body=json.dumps(riot_answer), status=404)

        test_client = Client()
        response = test_client.get(
            '/karma/get_summoner', {'summoner_name': '123false'})

        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), riot_answer)
