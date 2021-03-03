from unittest import TestCase
from main import FizzBuzz

class TestFizzBuzz(TestCase):
    def test_1を渡すと文字列1を返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行
        actual = fizzbuzz.convert(1)
        # 検証
        self.assertEqual(actual, "1")
