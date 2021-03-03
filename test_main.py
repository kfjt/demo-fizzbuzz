from unittest import TestCase
from main import FizzBuzz

class TestFizzBuzz(TestCase):
    def setUp(self):
        # 準備
        self.fizzbuzz = FizzBuzz()

    def test_数を文字列に変換する(self):
        with self.subTest("1を渡すと文字列1を返す"):
            # 実行＆検証
            self.assertEqual(self.fizzbuzz.convert(1), "1")

        with self.subTest("2を渡すと文字列2を返す"):
            # 実行＆検証
            self.assertEqual(self.fizzbuzz.convert(2), "2")

    def test_3の倍数のときは数の代わりにFizzに変換する(self):
        with self.subTest("3を渡すと文字列Fizzを返す"):
            # 実行＆検証
            self.assertEqual(self.fizzbuzz.convert(3), "Fizz")

    def test_5の倍数のときは数の代わりにBuzzに変換する(self):
        with self.subTest("5を渡すと文字列Buzzを返す"):
            # 実行＆検証
            self.assertEqual(self.fizzbuzz.convert(5), "Buzz")
