from unittest import TestCase

from Zadanie_3_Podzbiory import allBinary, subsets


class Test(TestCase):
    def test_all_binary(self):
        binary = []
        allBinary(3, binary, 0, [0, 0, 0])
        self.assertEqual(binary,
                         [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]],
                         "Blad testu funkcji allBinary")
        binary = []
        allBinary(2, binary, 0, [0, 0])
        self.assertEqual(binary, [[0, 0], [0, 1], [1, 0], [1, 1]], "Blad testu funkcji allBinary")
        with self.assertRaises(ValueError):
            allBinary(-1, binary, 0, [])
        with self.assertRaises(ValueError):
            allBinary(1, binary, -2, [])

    def test_subsets(self):
        self.assertEqual(subsets([1, 2]), [[], [2], [1], [1, 2]], "Niezdany test generowania podzbiorow")
        self.assertEqual(subsets([1]), [[], [1]], "Niezdany test generowania podzbiorow 1")
        self.assertEqual(subsets([]), [], "Niezdany test generowania podzbiorow 2")
        self.assertEqual(subsets([3, 2, 1]), [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]],
                         "Niezdany test generowania podzbiorow 3")
