import unittest

if __name__ == '__main__':
    test_dir = './testCase'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern= "test_*.py")
    unittest.TextTestRunner(verbosity=2).run(discover)

