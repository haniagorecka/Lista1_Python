from unittest import TestCase

from Zadanie_2_Czesc_Wspolna import shared, bubbleSort, switchToNext


class Test(TestCase):
    def test_shared(self):
        self.assertEqual(shared([1, 2, 3, 4], [3, 2]), [2, 3], "Blad testu funkcji")
        self.assertEqual(shared([], []), [], "Blad testu funkcji 2")
        self.assertEqual(shared([3, 3, 3, 3], [1, 1, 1]), [], "Blad testu funkcji 3")
        self.assertEqual(shared([3, 3, 3, 3, 5, -1, 2], [1, -1, 3, 5]), [-1, 3, 5], "Blad testu funkcji 4")
        self.assertEqual(shared([-0.5, 0.5], [0.5]), [0.5], "Blad testu funkcji 5")

    def test_bubbleSort(self):
        list = [9, 1, 2, 3, 9]
        bubbleSort(list)
        self.assertEqual(list, [1, 2, 3, 9, 9], "Blad testu funkcji sortujacej")
        list = [-1, 0, 9, -10]
        bubbleSort(list)
        self.assertEqual(list, [-10, -1, 0, 9], "Blad testu funkcji sortujacej 2")
        list = [0.5, -0.5, -1.2, 9.0]
        bubbleSort(list)
        self.assertEqual(list, [-1.2, -0.5, 0.5, 9.0], "Blad testu funkcji sortujacej 3")

    def test_switchToNext(self):
        list = [1, 2, 2, 3, 4, 5, 5]
        self.assertEqual(switchToNext(list, 1, 6), 3, "Blad testu funkcji switchToNext")
        self.assertEqual(switchToNext(list, 3, 6), 4, "Blad testu funkcji switchToNext 1")
        self.assertEqual(switchToNext(list, 4, 6), 5, "Blad testu funkcji switchToNext 2")
        self.assertEqual(switchToNext(list, 5, 6), 6, "Blad testu funkcji switchToNext")
        with self.assertRaises(ValueError):
            switchToNext(list, -1, 6)
        with self.assertRaises(ValueError):
            switchToNext(list, -2, -1)
        with self.assertRaises(OverflowError):
            switchToNext(list, 8, 6)
