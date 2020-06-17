from django.test import TestCase, Client
#from nose.tools import assert_true
from karma.utils.karma_compute import *

class TestKarmaComputation(TestCase):
    def test_wilson_score(self):
        upvotes = 10
        downvotes = 13
        expected_value = 0.25634368332198654
        self.assertEqual(wilson_score(upvotes, downvotes), expected_value)
