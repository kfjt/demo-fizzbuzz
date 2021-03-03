from unittest import TestCase
from main import FizzBuzz

class TestFizzBuzz(TestCase):
    def test_1を渡すと文字列1を返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行＆検証
        self.assertEqual(fizzbuzz.convert(1), "1")

    def test_2を渡すと文字列2を返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行＆検証
        self.assertEqual(fizzbuzz.convert(2), "2")

    def test_3を渡すと文字列Fizzを返す(self):
        # 準備
        fizzbuzz = FizzBuzz()
        # 実行＆検証
        self.assertEqual(fizzbuzz.convert(3), "Fizz")
