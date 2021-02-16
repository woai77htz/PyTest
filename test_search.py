import unittest


class Search():

    def search_fun(self):
        print("search")
        return True

class TestSearch(unittest.TestCase):

    def test_search1(self):
        print("testsearch1_case")
        search = Search()
        assert True == search.search_fun()


if __name__ == '__main__':
    unittest.main()