from primes import get_prime

def extended_euclidian_algorithm(a: int, b: int):
    """Löytää a:n ja b:n suurimman yhteisen tekijän, jota merkataan gcd(a,b), sekä Bezout kertoimet x ja y, joille pätee ax + by = gcd(a,b)

    Args:
        a: Toinen luvuista, joille etsitään suurinta yhteistä tekijää.
        b: Toinen luvuista, joka on a:n vastapari suurimman yhteisen tekijän etsimisessä.

    Returns:
        [int, int, int]: 3:n alkion lista, joka koostuu a:n Bezout kertoimesta, b:n Bezout kertoimesta ja luvusta gcd(a,b).
    """
    x = [1, 0, a]
    y = [0, 1, b]

    while y[2] > 0:
        k = x[2] // y[2]
        for i in range(3):
            x[i] -= k * y[i]
        
        temp = x
        x = y
        y = temp

    return x
    

def generate_keys():
    """Luo RSA algoritmissa käytettävän julkis- ja yksityisavaimen

    Returns:
        Kaksi (int, int) tuplea, joista ensimmäinen on julkinen avain ja toinen yksityinen avain. 
    """

    e = 65537

    while True:
        p = get_prime()
        q = get_prime()

        N = p*q

        phi_N = (p-1)*(q-1)

        x, _, gcd = extended_euclidian_algorithm(e, phi_N)

        if gcd == 1:
            break

    d = x % phi_N

    public_key = (N, e)
    private_key = (N, d)

    return public_key, private_key