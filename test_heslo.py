import unittest
from unittest import TestCase
from heslo import KontrolaHesla


class TestKontrolaHesla(unittest.TestCase):
    def test_kontrola_hesla(self):
        validator= KontrolaHesla()
        self.assertTrue(validator.kontroluj("abcd123"))

    def test_kratke_heslo(self):
        validator = KontrolaHesla()
        self.assertTrue(validator.kontroluj("ab2dddddd"))

    def test_prazdne_heslo(self):
        validator = KontrolaHesla()
        self.assertTrue(validator.kontroluj("1jjjjdd"))


