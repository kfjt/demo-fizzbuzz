from unittest import TestCase
from main import FizzBuzz

class TestFizzBuzz:
    class Test_convertメソッドは数を文字列に変換する:
        class _3の倍数のときは数の代わりにFizzに変換する(TestCase):
            def test_3を渡すと文字列Fizzを返す(self):
                # 準備
                self.fizzbuzz = FizzBuzz()
                # 実行＆検証
                self.assertEqual(self.fizzbuzz.convert(3), "Fizz")

        class _5の倍数のときは数の代わりにBuzzに変換する(TestCase):
            def test_5を渡すと文字列Buzzを返す(self):
                # 準備
                self.fizzbuzz = FizzBuzz()
                # 実行＆検証
                self.assertEqual(self.fizzbuzz.convert(5), "Buzz")

        class その他の数のときはそのまま文字列に変換する(TestCase):
            def setUp(self):
                # 準備
                self.fizzbuzz = FizzBuzz()

            def test_1を渡すと文字列1を返す(self):
                # 実行＆検証
                self.assertEqual(self.fizzbuzz.convert(1), "1")

if __name__ == "__main__":
    from unittest import main

    main(verbosity=2, module=TestFizzBuzz.Test_convertメソッドは数を文字列に変換する)
