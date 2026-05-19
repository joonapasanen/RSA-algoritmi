import unittest
from primes import sample_odd_number, miller_rabin_test

class TestSampleOddNumber(unittest.TestCase):
    def setUp(self):
        self.num = sample_odd_number()

    def test_number_is_odd(self):
        self.assertEqual(self.num % 2, 1)

    def test_number_is_below_upper_bound(self):
        self.assertEqual(self.num <= 2**1024, True)

    def test_number_is_above_lower_bound(self):
        self.assertEqual(self.num >= 2**1023, True)

class TestMillerRabinTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_small_even_prime(self):
        self.assertEqual(miller_rabin_test(2), False)

    def test_small_odd_prime(self):
        self.assertEqual(miller_rabin_test(7), True)

    def test_small_odd_composite(self):
        self.assertEqual(miller_rabin_test(15), False)

    def test_large_odd_prime(self):
        self.assertEqual(miller_rabin_test(685050345688069904033056649023), True)

    def test_large_odd_composite(self):
        self.assertEqual(miller_rabin_test(804050816046724198023053199073), False)

    def test_small_carmichael_number(self):
        self.assertEqual(miller_rabin_test(561), False)

    def test_large_carmichael_number(self):
        self.assertEqual(miller_rabin_test(2810864562635368426005268142616001), False)
