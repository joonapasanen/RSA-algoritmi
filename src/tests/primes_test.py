import unittest
import sympy
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
        self.primes = [7, 142859932996443634508535050364485528373793963900852491689011733577519511274967690105057989824570020373317992890439334205771842469368620100230267508675841959743535278766127760236838842128350710107009728684079095534576230858312248157016275930309005893716922340345323766300884684083411223999524400732385144209387]
        self.carmichaels = [561, 90054786234783819025631878025225614062389252471419903108640546958944923768206111017039041920525582144105851593698231918498750612535533694965236268066088057885922919851112813991350567509714061176292639643543056943279430146904471546655127636722878405751328582141664779275610072068356859597909337963447078047721]
        self.composites = [4, 97609266489791738895915350821396969686117620685956708310456580620548873483929992998604639705668823316398495978864464006963734560319145045801854033368896198400704513576063987645371814195551289756873438975663453553987699249265808747144622085441935988875228155235962375803917894223621038246687834883496302521997]

    def test_with_2(self):
        self.assertEqual(miller_rabin_test(2), False)

    def test_primes(self):
        for prime in self.primes:
            self.assertEqual(miller_rabin_test(prime), True)

    def test_carmichaels(self):
        # Carmichaelin luvut ovat lukujoukko, joka huijaa yksinkertaiset alkulukutestit kuten Fermat'n testin.
        for carmichael in self.carmichaels:
            self.assertEqual(miller_rabin_test(carmichael), False)
                
    def test_composites(self):
        for composite in self.composites:
            self.assertEqual(miller_rabin_test(composite), False)

class TestGetPrime(unittest.TestCase):
    def setUp(self):
        self.prime = get_prime()

    def test_number_is_odd(self):
        self.assertEqual(self.prime % 2, 1)

    def test_number_is_below_upper_bound(self):
        self.assertEqual(self.prime <= 2**1024, True)

    def test_number_is_above_lower_bound(self):
        self.assertEqual(self.prime >= 2**1023, True)

    def test_is_prime(self):
        self.assertEqual(sympy.isprime(self.prime), True)