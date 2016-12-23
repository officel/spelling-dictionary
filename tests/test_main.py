import os
import unittest


class TestAllDirectory(unittest.TestCase):
    # all ディレクトリ中の all.dic の中身をテスト
    def setUp(self):
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.f = open(os.path.abspath(os.path.join(root_path, "all", "all.dic")), "rt", encoding="utf-8", newline="\n")

    def tearDown(self):
        self.f.close()

    def test_all(self):
        # ファイルの中身を全て読込、検査対象の文字列が存在することを確認する
        data1 = self.f.read()
        lines1 = data1.split("\n")
        self.assertIn('elasticache', lines1)  # from aws
        self.assertIn('documentdb', lines1)  # from azure
        self.assertIn('gitglossary', lines1)  # from git
        self.assertIn('stackdriver', lines1)  # from google
        self.assertIn('dotcover', lines1)  # from jetbrains
        self.assertIn('piyo', lines1)  # from metasyntactic_variable
        self.assertIn('startuml', lines1)  # from plantuml
        self.assertIn('gitter', lines1)  # from web service
        self.assertIn('toctree', lines1)  # from sphinx
        self.assertIn('jira', lines1)  # from atlassian


if __name__ == '__main__':
    unittest.main()
