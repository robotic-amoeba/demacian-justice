from django.test import TestCase, Client
from karma.models import Summoner
from nose.tools import assert_true
import httpretty
import json
import re

class SummonerAPITestCase(TestCase):
    RIOT_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/.*"
    def setUp(self):
        Summoner.objects.create(puuid=1, upvotes=4)

    @httpretty.activate
    def test_client_get_success(self):
        """GET request to client successes"""
        summoner_info = {'accountId': '6c-2t4GjYiljgGoz-Rq6xsEPcupymkR8_kjWgamIxPUPag',
                         'puuid': '1',
                         'name': 'Kixmo',
                         'profileIconId': 4227,
                         'revisionDate': 1586719398000,
                         'summonerLevel': 195,
                         'upvotes': 4,
                         'downvotes': 0,
                         'karma': 4}

        httpretty.register_uri(httpretty.GET, re.compile(SummonerAPITestCase.RIOT_URL),
                               body=json.dumps(summoner_info))

        test_client = Client()
        response = test_client.get(
            '/karma/get_summoner', {'name': 'feeder_sticks', 'server': 'euw1'})

        response_dict = json.loads(response.content)
        response_dict.pop('created_at')
        response_dict.pop('updated_at')
        response_dict.pop('id')

        self.assertEqual(response_dict, summoner_info)
        self.assertEqual(response.status_code, 200)

    @httpretty.activate
    def test_client_get_success_summoner_not_exist(self):
        """GET request to client successes"""
        summoner_info = {'accountId': '6c-2t4GjYiljgGoz-Rq6xsEPcupymkR8_kjWgamIxPUPag',
                         'puuid': '7',
                         'name': 'Kixmo',
                         'profileIconId': 4227,
                         'revisionDate': 1586719398000,
                         'summonerLevel': 195,
                         'upvotes': 0,
                         'downvotes': 0,
                         'karma': 0}

        httpretty.register_uri(httpretty.GET, re.compile(SummonerAPITestCase.RIOT_URL),
                               body=json.dumps(summoner_info))

        test_client = Client()
        response = test_client.get(
            '/karma/get_summoner', {'name': 'feeder_sticks', 'server': 'euw1'})

        response_dict = json.loads(response.content)

        self.assertEqual(response_dict, summoner_info)
        self.assertEqual(response.status_code, 200)

    @httpretty.activate
    def test_client_get_server_error(self):
        """GET request to client returns server error"""
        httpretty.register_uri(httpretty.GET, re.compile(SummonerAPITestCase.RIOT_URL),
                               status=500)

        test_client = Client()
        response = test_client.get(
            '/karma/get_summoner', {'name': 'feeder_sticks', 'server': 'euw1'})

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
            '/karma/get_summoner', {'name': '123false', 'server': 'euw1'})

        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), riot_answer)

class KarmaViewsTest(TestCase):
    def setUp(self):
        Summoner.objects.create(puuid=1, upvotes=4)

    def test_vote_existing_summoner(self):
        """Votes are performed properly for an existing summoner"""
        summoner_info = {'puuid': '1',
                         'upvotes': 5,
                         'downvotes': 0,
                         'karma': 5}

        test_client = Client()
        response = test_client.post(
            '/karma/vote', {'summoner_uuid': 1, 'vote': 'upvote'}, content_type="application/json")

        response_dict = json.loads(response.content)
        response_dict.pop('id')
        self.assertEqual(response_dict, summoner_info)

    def test_vote_creating_summoner(self):
        """Summoner is created if does not exist and the vote is added"""
        summoner_info = {'puuid': '24',
                         'upvotes': 0,
                         'downvotes': 1,
                         'karma': -1}

        test_client = Client()
        response = test_client.post(
            '/karma/vote', {'summoner_uuid': '24', 'vote': 'downvote'}, content_type="application/json")

        response_dict = json.loads(response.content)
        response_dict.pop('id')
        self.assertEqual(response_dict, summoner_info)
