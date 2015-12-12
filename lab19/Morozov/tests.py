from unittest import TestCase
from main import palindrome

__author__ = 'vks'


class Test(TestCase):
    def test_sample1(self):
        s = "abca"
        self.assertEqual(palindrome(s), "aba")

    def test_sample2(self):
        s = "babcad"
        self.assertEqual(palindrome(s), "bab")

    def test_empty(self):
        s = ""
        self.assertEqual(palindrome(s), "")

    def test_trivial1(self):
        s = "a"
        self.assertEqual(palindrome(s), "a")

    def test_trivial2(self):
        s = "ab"
        self.assertEqual(palindrome(s), "a")

    def test_trivial3(self):
        s = "abacabadabacaba"
        self.assertEqual(palindrome(s), "abacabadabacaba")

    def test_small(self):
        s = "abacabazzzzzzz"
        self.assertEqual(palindrome(s), "abacaba")

    def test_small2(self):
        s = "abacabazzzzzzzz"
        self.assertEqual(palindrome(s), "zzzzzzzz")

    def test_medium1(self):
        s = "slatkor zarepyo tqenet opera rotas"
        self.assertEqual(palindrome(s), "sator arepo tenet opera rotas")

    def test_medium2(self):
        s = "abbazfghijklmza"
        self.assertEqual(palindrome(s), "azfza")

    def test_medium3(self):
        s = "jqwerqpqoiwewqs"
        self.assertEqual(palindrome(s), "qweqpqewq")

    def test_medium4(self):
        s = "yzaghbicjkdlefmnopeqdrsctbuvawx"
        self.assertEqual(palindrome(s), "abcdefedcba")

    def test_medium5(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(palindrome(s), "a")

    def test_medium6(self):
        s = "ghgaxybtltcmdinnefuvjegkodpcwozbzqqarjj"
        self.assertEqual(palindrome(s), "abcdefedcba")

    def test_medium7(self):
        s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.assertEqual(palindrome(s), "aba")
