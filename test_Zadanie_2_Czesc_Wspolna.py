from unittest import TestCase

from Zadanie_2_Czesc_Wspolna import shared


class Test(TestCase):
    def test_shared(self):
        self.assertEqual(shared([1,2,3,4], [3,2]), [2,3], "Blad testu funkcji")
