from unittest import TestCase

from Zadanie_6_DNA import komplement, transkrybuj, transluj


class Test(TestCase):
    def test_komplement(self):
        self.assertEqual(komplement("agggactga"), "TCAGTCCCT", "Blad testu funkcji komplement" )
        self.assertEqual(komplement("tttag"), "CTAAA", "Blad testu funkcji komplement 1")
        with self.assertRaises(ValueError):
            komplement("")
        with self.assertRaises(ValueError):
            komplement(" ")
        with self.assertRaises(ValueError):
            komplement("J")
        with self.assertRaises(TypeError):
            komplement(2)


    def test_transkrybuj(self):
        self.assertEqual(transkrybuj("acgat"), "AUCGU", "Blad testu funkcji komplement")
        self.assertEqual(transkrybuj("tttag"), "CUAAA", "Blad testu funkcji komplement 1")
        with self.assertRaises(ValueError):
            transkrybuj("")
        with self.assertRaises(ValueError):
            transkrybuj(" ")
        with self.assertRaises(ValueError):
            transkrybuj("J")
        with self.assertRaises(TypeError):
            transkrybuj(2)

    def test_transluj(self):
        self.assertEqual(transluj("AUUUCAC"), "Ile Ser ", "Blad funkcji transkrybuj")
        self.assertEqual(transluj("UAG"), " ", "Blad funkcji transkrybuj 1")
        self.assertEqual(transluj("auagagagaggaua"), "Ile Glu Arg Gly ", "Blad funkcji transkrybuj 2")
        with self.assertRaises(ValueError):
            transluj("")
        with self.assertRaises(ValueError):
            transluj("ABCD")
        with self.assertRaises(TypeError):
            transluj(2)
