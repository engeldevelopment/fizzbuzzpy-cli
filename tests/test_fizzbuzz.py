from unittest import TestCase

from fizzbuzz import calculator


class TestFizzBuzz(TestCase):
    def test_if_number_is_divisible_by_three_should_show_fizz(self):
        self.assertEqual("fizz", calculator.value_of(3))
        self.assertEqual("fizz", calculator.value_of(9))
        self.assertEqual("fizz", calculator.value_of(12))

    def test_if_number_is_divisible_by_five_should_show_buzz(self):
        self.assertEqual("buzz", calculator.value_of(5))
        self.assertEqual("buzz", calculator.value_of(10))
        self.assertEqual("buzz", calculator.value_of(25))

    def test_if_number_is_divisible_by_three_and_five_should_show_fizzbuzz(self):
        self.assertEqual("fizzbuzz", calculator.value_of(15))
        self.assertEqual("fizzbuzz", calculator.value_of(30))

    def test_if_number_is_not_divisible_by_three_and_five_should_show_fizzbuzz(self):
        self.assertEqual("1", calculator.value_of(1))
        self.assertEqual("2", calculator.value_of(2))
