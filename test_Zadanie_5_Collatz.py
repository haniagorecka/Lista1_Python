from unittest import TestCase

from Zadanie_5_Collatz import collatz


class Test(TestCase):
    def test_collatz(self):
        self.assertEqual(collatz(10), [10, 5, 16, 8], "Blad testu funkcji")
        self.assertEqual(collatz(4), [], "Blad testu funkcji 1")
        self.assertEqual(len(collatz(3092)), 121, "Blad testu funkcji 1")
        with self.assertRaises(ValueError):
            collatz(-1)
        with self.assertRaises(TypeError):
            collatz(1.9)



