import unittest


class TestMain(unittest.TestCase):
    def test_all(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
