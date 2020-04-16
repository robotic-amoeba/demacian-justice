import unittest

def SummonerAPI_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(SummonerAPITestCase('test_client_get_success'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(SummonerAPI_test_suite())
