import  selenium
import  requests
import  unittest

class TestDome(unittest.TestCase):

    def test_abc(self):
        print("abc")

    def test_upper(self):
        self.assert_('foo'.upper(),'foo')


    def test_isupper(self):
        self.assertTrue('Foo'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello word'
        self.assertEqual(s.split(),['hello','word'])

        with self.assertRaises(TypeError):
            s.split(2)