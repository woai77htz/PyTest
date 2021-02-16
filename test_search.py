import datetime
import unittest
from time import sleep


class Search():

    def search_fun(self):
        print("search")
        return True


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print("setUpClass:"+otherStyleTime)
        print('setUp class')
        cls.search = Search()

    def test_search1(self):
        sleep(1)
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print("test_search1:"+otherStyleTime)
        print("testsearch1_case")
        assert True == self.search.search_fun()

    def test_search2(self):
        sleep(1)
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print("test_search2:"+otherStyleTime)
        print("testsearch2_case")
        assert True == self.search.search_fun()

    def test_search3(self):
        sleep(1)
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print("test_search3:"+otherStyleTime)
        print("testsearch3_case")
        assert True == self.search.search_fun()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(1)
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print("tearDownClass:"+otherStyleTime)
        print("tearDown Class")

    def test_equql(self):
        self.assertEqual(1,1, "1==1")

    def test_notequql(self):
        self.assertNotEqual(1,2, "1 != 2")


if __name__ == '__main__':
    unittest.main()
