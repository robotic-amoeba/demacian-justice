from django.test import TestCase, Client
from karma.models import Summoner
import httpretty
import json

class KarmaViewsTest(TestCase):
    def setUp(self):
        Summoner.objects.create(name="feedersticks", puuid=1, upvotes=4)

    def test_vote_existing_summoner(self):
        """Votes are performed properly for an existing summoner"""
        summoner_info = {'name': 'feedersticks',
                         'puuid': '1',
                         'upvotes': 5,
                         'downvotes': 0}

        test_client = Client()
        response = test_client.post(
            '/karma/vote', {'summoner_uuid': 1, 'vote': 'upvote'})

        response_dict = json.loads(json.loads(response.content))
        response_dict.pop('created_at')
        response_dict.pop('updated_at')
        response_dict.pop('id')
        self.assertEqual(response_dict, summoner_info)

    def test_vote_creating_summoner(self):
        """Summoner is created if does not exist and the vote is added"""
        summoner_info = {'name': '',
                         'puuid': '24',
                         'upvotes': 0,
                         'downvotes': 1}

        test_client = Client()
        response = test_client.post(
            '/karma/vote', {'summoner_uuid': 24, 'vote': 'downvote'})

        response_dict = json.loads(json.loads(response.content))
        response_dict.pop('created_at')
        response_dict.pop('updated_at')
        response_dict.pop('id')
        self.assertEqual(response_dict, summoner_info)
