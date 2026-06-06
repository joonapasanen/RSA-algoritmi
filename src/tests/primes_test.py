import unittest
import math
from primes import sample_odd_number, miller_rabin_test, sieve_of_eratosthenes, get_prime

class TestSampleOddNumber(unittest.TestCase):
    def setUp(self):
        self.nums = [sample_odd_number() for _ in range(100)]

    def test_number_is_odd(self):
        for num in self.nums:
            self.assertEqual(num % 2, 1)

    def test_number_is_below_upper_bound(self):
        for num in self.nums:
            self.assertEqual(num <= 2**1024, True)

    def test_number_is_above_lower_bound(self):
        for num in self.nums:
            self.assertEqual(num >= 2**1023, True)

class TestSieveOfEratosthenes(unittest.TestCase):
    def setUp(self):
        self.primes_list = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
            101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 
            197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
            311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
            431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499
        ]

    def test_primes_less_than_or_equal_100(self):
        self.assertEqual(sieve_of_eratosthenes(100), self.primes_list[:25])

    def test_primes_less_than_or_equal_500(self):
        self.assertEqual(sieve_of_eratosthenes(500), self.primes_list) 

    def test_input_is_1(self):
        self.assertEqual(sieve_of_eratosthenes(1), [])
    
    def test_negative_input(self):
        self.assertEqual(sieve_of_eratosthenes(-21), [])


class TestMillerRabinTest(unittest.TestCase):
    def setUp(self):
        self.primes = [7, 13, 685050345688069904033056649023]
        self.carmichaels = [561, 2810864562635368426005268142616001]
        self.composites = [4, 15, 804050816046724198023053199073]

    def test_with_2(self):
        self.assertEqual(miller_rabin_test(2), False)

    def test_primes(self):
        for prime in self.primes:
            self.assertEqual(miller_rabin_test(prime), True)

    def test_carmichaels(self):
        # Carmichaelin numerot ovat numerojoukko, joka huijaa yksinkertaiset alkuluku testit kuten Fermat'n testin.
        for carmichael in self.carmichaels:
            self.assertEqual(miller_rabin_test(carmichael), False)
                
    def test_composites(self):
        for composite in self.composites:
            self.assertEqual(miller_rabin_test(composite), False)

class TestGetPrime(unittest.TestCase):
    def setUp(self):
        self.prime = get_prime()

    def test_is_coprime_prime_to_another_prime(self):
        for x in [2, 5, 11, 13, 29, 41, 61, 67, 83, 97]:
            self.assertEqual(math.gcd(x, self.prime), 1)
        