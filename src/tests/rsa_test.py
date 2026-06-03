import unittest
from rsa import generate_keys, extended_euclidian_algorithm

class TestExtendedEuclidianAlgorithm(unittest.TestCase):
    def setUp(self):
        pass

    def test_gcd_784_and_12056_bezout_coefficient_1(self):
        self.assertEqual(692, extended_euclidian_algorithm(784, 12056)[0])
    
    def test_gcd_784_and_12056_bezout_coefficient_2(self):
        self.assertEqual(-45, extended_euclidian_algorithm(784, 12056)[1])

    def test_gcd_784_and_12056_gcd(self):
        self.assertEqual(8, extended_euclidian_algorithm(784, 12056)[2])

    def test_gcd_two_primes(self):
        self.assertEqual(1, extended_euclidian_algorithm(7, 23)[2])

    def test_gcd_2_and_large_power_of_two(self):
        self.assertEqual(2, extended_euclidian_algorithm(2, 2**123)[2])

class TestGenerateKeys(unittest.TestCase):
    def setUp(self):
        self.public_key, self.private_key = generate_keys()

    def test_public_key_tuple_length(self):
        public_key_len = len(self.public_key)
        self.assertEqual(public_key_len, 2)

    def test_private_key_tuple_length(self):
        public_key_len = len(self.public_key)
        self.assertEqual(public_key_len, 2)

    def test_keys_same_N(self):
        self.assertEqual(self.public_key[0], self.private_key[0])
