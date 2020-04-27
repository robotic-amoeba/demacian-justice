from django.test import TestCase
from karma.models import Summoner

class AnimalTestCase(TestCase):
    def setUp(self):
        Summoner.objects.create(name="feedersticks", puuid=1)

    def test_summoners_are_saved(self):
        """Summoners are saved properly"""
        summoner = Summoner.objects.get(name="feedersticks")
        self.assertEqual(summoner.name, 'feedersticks')
