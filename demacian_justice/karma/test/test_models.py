from django.test import TestCase
from karma.models import Summoner

class SummonerTestCase(TestCase):
    def setUp(self):
        Summoner.objects.create(puuid=1, upvotes=4)

    def test_summoners_can_be_retrieved(self):
        """Summoners are retrieved properly"""
        summoner = Summoner.objects.get(puuid="1")
        self.assertEqual(summoner.puuid, '1')
        self.assertEqual(summoner.upvotes, 4)

    def  test_vote(self):
        """Summoners votes are increased properly"""
        summoner = Summoner.objects.get(puuid=1)
        summoner.vote("upvote")
        self.assertEqual(summoner.upvotes, 5)
