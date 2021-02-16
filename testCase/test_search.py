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

class TestSearch1(unittest.TestCase):
    def test_search4(self):
        print("test_search4")


if __name__ == '__main__':
    # 方法一，执行当前文件所有unittest测试用例，全部执行
    # unittest.main()
    # 方法二，执行指定 测试用例，将要执行的测试用例添加到测试套件里面，批量执行测试方法
    # 创建一个测试套件， testsuite
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_search1"))
    # unittest.TextTestRunner().run(suite)

    # 方法三，执行某个测试类，将测试类添加到测试套件里面，批量执行测试类
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    suite = unittest.TestSuite([suite2,suite3])
    unittest.TextTestRunner(verbosity=2).run(suite)
