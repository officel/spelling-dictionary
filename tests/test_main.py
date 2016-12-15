import os
import unittest


class TestAllDirectory(unittest.TestCase):

    def setUp(self):
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.f = open(os.path.abspath(os.path.join(root_path, "all", "all.dic")), "rt", encoding="utf-8", newline="\n")

    def tearDown(self):
        self.f.close()

    def test_all(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
