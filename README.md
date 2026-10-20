# RSA Cryptosystem from Scratch

A from-scratch implementation of 2048-bit RSA in pure Python, with no cryptography libraries. It covers key generation, encryption and decryption. Every building block is implemented by hand: random prime generation, a small-prime sieve, the Miller–Rabin primality test and the extended Euclidean algorithm.

Built as the project for the *Algorithms and AI* project course at the University of Helsinki.

## Features

- **2048-bit keys** generated from two random 1024-bit probable primes, with public exponent `e = 65537`
- **Fast prime generation:** random odd candidates are first trial-divided by the 500 smallest primes (from a Sieve of Eratosthenes), and only survivors go through 40 rounds of Miller–Rabin. That gives an error probability below 4⁻⁴⁰.
- **Private exponent** computed with the extended Euclidean algorithm (modular inverse of `e` mod φ(N))
- **Cryptographically secure randomness** for candidate primes via Python's `secrets` module
- **Interactive CLI** for encrypting messages into a queue and decrypting them with the private key

## Algorithms and complexity

| Algorithm | Purpose | Time | Space |
| --- | --- | --- | --- |
| Sieve of Eratosthenes | Small primes for trial division | O(n log log n) | O(n) |
| Miller–Rabin (k rounds) | Probabilistic primality test | O(k · b³), b = bits | O(b) |
| Extended Euclidean algorithm | Modular inverse for the private key | O(log min(a, b)) | O(1) |

Encryption and decryption use modular exponentiation (`pow(m, e, N)`).

## Project structure

```
src/
├── primes.py        # random odd sampling, sieve, Miller–Rabin, prime generation
├── rsa.py           # extended Euclid, key generation, encrypt / decrypt
├── main.py          # interactive command-line interface
└── tests/
    ├── primes_test.py      # unit tests for prime generation
    ├── rsa_test.py         # unit + integration tests for keys and Euclid
    └── end_to_end_test.py  # encrypt → decrypt round trip
dokumentaatio/       # course documentation (in Finnish)
```

## Getting started

Requires Python 3.12+ and [Poetry](https://python-poetry.org/).

```bash
git clone https://github.com/joonapasanen/RSA-algoritmi.git
cd RSA-algoritmi
poetry install
poetry run python src/main.py
```

The program generates a key pair and shows your private exponent. Then:

- `s`: type a message, which is encrypted with the public key and added to the queue
- `r`: enter the private key to decrypt the most recent message
- `q`: quit

## Testing

The test suite has three levels:

- **Unit tests:** odd-number sampling stays in [2¹⁰²³, 2¹⁰²⁴); the sieve matches known prime lists; Miller–Rabin correctly classifies primes, composites and **Carmichael numbers** (composites that fool the Fermat test); extended Euclid returns correct Bézout coefficients, including for 1024-bit inputs.
- **Integration tests:** generated primes are verified independently with SymPy, and key pairs are checked for structure and a shared modulus. Large test primes are verified against [factordb.com](https://factordb.com).
- **End-to-end tests:** a message survives the full encrypt → decrypt round trip.

```bash
poetry run coverage run --branch -m pytest
poetry run coverage report -m
```

Branch coverage of the core modules is 100% for `primes.py` and 97% for `rsa.py`. The interactive CLI in `main.py` is not unit-tested.

## Limitations

This is an educational implementation of **textbook RSA** and is not suitable for real-world use:

- No padding scheme (such as OAEP), so encryption is deterministic and malleable
- Messages are encoded directly as integers, so they must be shorter than the modulus (about 255 bytes)
- No constant-time arithmetic and no protection against side-channel attacks
- Keys are held in memory only and are not saved or loaded

## Documentation

Detailed course documentation (specification, implementation report, testing report and weekly reports) is in [`dokumentaatio/`](./dokumentaatio), in Finnish.
