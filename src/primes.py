import secrets
import random

def sample_odd_number():
    """Luo parittoman kokonaisluvun väliltä [2^1023, 2^1024) satunnaisesti.

    Returns:
        Pariton kokonaisluku väliltä [2^1023, 2^1024).
    """

    upper_bound = 2**1024
    lower_bound = 2**1023

    random_num = secrets.randbelow(upper_bound - lower_bound) + lower_bound
    
    if random_num % 2 == 0:
        random_num += 1

    return random_num

def sieve_of_eratosthenes(limit: int):
    """Etsii jokaisen alkuluvun väliltä [0, limit] tehokkaasti.

    Args:
        limit: Kokonaisluku, joka on suurempi kuin 1. Yläraja alkuluvuille joita algoritmi etsii.

    Returns: Lista alkuluvuista välillä [0, limit].
    """

    if limit < 2:
        return []
    
    numbers = [True for _ in range(0, limit + 1)]
    numbers[0] = numbers[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if numbers[i] == True:
            j = 0
            while i**2 + j*i <= limit:
                numbers[i**2 + j*i] = False
                j += 1

    primes = [i for i, is_prime in enumerate(numbers) if is_prime]

    return primes

def miller_rabin_test(n: int, rounds=40):
    """Miller-Rabin-testi antaa stokastisen arvion siitä onko n alkuluku. 
       40 kierrosta ilmoittaa oikean alkuluvun todennäköisyydellä 1 - (0.25)**40, joka on noin 0.999...

    Args:
        n: Pariton luku, jota testi stokastisesti arvioi olevan alkuluku.
        rounds: Testissä käytettävien kierrosten lukumäärä.

    Returns:
        True, jos n on testin mielestä alkuluku, muuten False.
    """

    if n % 2 == 0:
        print("Käytä paritonta lukua syötteenä.")
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(rounds):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if x != 1:
            return False

    return True

def get_prime():
    """Löytää todennäköisen alkuluvun tehokkaasti tarkastamalla ensin onko luvulla pieniä alkuluku tekijöitä 
       ja käyttäen sitten Miller-Rabin-algoritmia.

    Returns:
        int: Todennäköinen alkuluku.
    """
    small_primes_list = sieve_of_eratosthenes(500)

    p = None
    while not p:
        num = sample_odd_number()

        for small_prime in small_primes_list:
            if num % small_prime == 0:
                break
 
        if not miller_rabin_test(num, rounds=10):
            continue
        else:
            p = num

    return p