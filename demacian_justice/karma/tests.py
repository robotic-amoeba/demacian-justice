import unittest

def SummonerAPI_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(SummonerAPITestCase('test_client_get_success'))
    suite.addTest(SummonerAPITestCase('test_client_get_server_error'))
    suite.addTest(SummonerAPITestCase('test_client_get_not_found'))
    return suite

def SummonerModel_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(SummonerTestCase('test_summoners_can_be_retrieved'))
    suite.addTest(SummonerTestCase('test_vote'))
    return suite

def KarmaViews_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(KarmaViewsTest('test_vote_existing_summoner'))
    suite.addTest(KarmaViewsTest('test_vote_creating_summoner'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(SummonerAPI_test_suite())
    runner.run(SummonerModel_test_suite())
    runner.run(KarmaViews_test_suite())
