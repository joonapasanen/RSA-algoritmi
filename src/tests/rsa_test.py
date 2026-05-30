import unittest
from rsa import generate_keys, extended_euclidian_algorithm

class TestExtendedEuclidianAlgorithm(unittest.TestCase):
    def setUp(self):
        pass

    def test_gcd_784_and_12056(self):
        self.assertEqual(8, extended_euclidian_algorithm(784, 12056)[2])

class TestGenerateKeys(unittest.TestCase):
    def setUp(self):
        pass
    