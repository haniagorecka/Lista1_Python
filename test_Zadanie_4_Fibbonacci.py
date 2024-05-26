from unittest import TestCase

from Zadanie_4_Fibbonacci import fiboRec, fibo


class Test(TestCase):
    def test_fibo_rec(self):
        self.assertEqual(fiboRec(4), [0, 1, 1, 2], "Blad testu funkcji rekurencyjnej ciagu fibonacciego")
        self.assertEqual(fiboRec(9), [0, 1, 1, 2, 3, 5, 8, 13, 21],
                         "Blad testu funkcji rekurencyjnej ciagu fibonacciego 1")
        with self.assertRaises(ValueError):
            fiboRec(-9)

    def test_fibo(self):
        self.assertEqual(fibo(4), [0, 1, 1, 2], "Blad testu funkcji iteracyjnej ciagu fibonacciego")
        self.assertEqual(fibo(9), [0, 1, 1, 2, 3, 5, 8, 13, 21],
                         "Blad testu funkcji iteracyjnej ciagu fibonacciego 1")
        with self.assertRaises(ValueError):
            fiboRec(-10)
