from unittest import TestCase
from kalkulacka import Kalkulacka

class TestKalkulacka(TestCase):
    def test_secti(self):
        kalkulacka = Kalkulacka()
        self.assertEqual(5, kalkulacka.secti(2,3))
