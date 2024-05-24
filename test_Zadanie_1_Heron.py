from unittest import TestCase

from Zadanie_1_Heron import heron


class Test(TestCase):
    def test_heron(self):
        self.assertAlmostEqual(heron(2,2,2), 1.732, 3, "Wrong test result in test 1")
        self.assertAlmostEqual(heron(10,10,2),9.95, 2, "Wrong test result in test 2")
        with self.assertRaises(ValueError):
            heron(-1, 1,1)
        with self.assertRaises(ValueError):
            heron(1, 0,1)
        with self.assertRaises(ValueError):
            heron(1, 1,10)



