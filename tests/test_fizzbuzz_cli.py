from unittest import TestCase

from click.testing import CliRunner

from fizzbuzz.scripts.fizzbuzz import fizzbuzz


class TestFizzBuzzCLI(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_debe_devolver_el_resultado_cuando_le_pase_un_numero(self):
        result = self.runner.invoke(fizzbuzz, ["3"])
        self.assertIn("fizz", result.output)

        result = self.runner.invoke(fizzbuzz, ["5"])
        self.assertIn("buzz", result.output)

        result = self.runner.invoke(fizzbuzz, ["15"])
        self.assertIn("fizzbuzz", result.output)

        result = self.runner.invoke(fizzbuzz, ["1"])
        self.assertIn("1", result.output)

    def test_deberia_darme_un_error_cuando_no_paso_un_numero(self):
        result = self.runner.invoke(fizzbuzz, [""])
        self.assertIn(
            "Invalid value for 'NUMBER':  is not a valid integer", result.output
        )
