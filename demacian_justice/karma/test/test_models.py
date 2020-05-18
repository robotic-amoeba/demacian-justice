from django.test import TestCase
from karma.models import Summoner

class SummonerTestCase(TestCase):
    def setUp(self):
        Summoner.objects.create(name="feedersticks", puuid=1, upvotes=4)

    def test_summoners_are_saved(self):
        """Summoners are saved properly"""
        summoner = Summoner.objects.get(name="feedersticks")
        self.assertEqual(summoner.name, 'feedersticks')

    def  test_vote(self):
        """Summoners votes are increased properly"""
        summoner = Summoner.objects.get(puuid=1)
        summoner.vote("upvote")
        self.assertEqual(summoner.upvotes, 5)
