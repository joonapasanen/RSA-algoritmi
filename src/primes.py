import secrets
import random

def sample_odd_number():
    """Luo parittoman kokonaisluvun väliltä [2^1023, 2^1024] satunnaisesti.

    Returns:
        Pariton kokonaisluku väliltä [2^1023, 2^1024].
    """

    upper_bound = 2**1024
    lower_bound = 2**1023

    random_num = 0
    while random_num % 2 == 0:
        random_num = secrets.randbelow(upper_bound - lower_bound) + lower_bound

    return random_num

def miller_rabin_test(n: int, rounds=10):
    """Miller-Rabin-testi antaa stokastisen arvion siitä onko n alkuluku.

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
