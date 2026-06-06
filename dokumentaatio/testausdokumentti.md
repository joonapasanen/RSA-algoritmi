# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

![alt text](![alt text](kuvat/kattavuusraportti.png))

## Mitä on testattu ja minkälaisilla syötteillä

Satunnaisten parittomien lukujen luonti väliltä [2^1023, 2^1024) (funktio sample_odd_number primes.py moduulista). Yksikkötestit testaavat että luku on pariton, sekä että luku kuuluu halutulle intervallille. Funktion toimivuus testataan lisäämällä sata sen luomaa numeroa listaan ja tarkistamalla jokaiselle numerolle listalla, että yllä mainitut testit läpäisevät.

## Miten testit voi toistaa?

Testit voi suorittaa komennolla: poetry run coverage run --branch -m pytest

Ja tulostaa konsoliin komennolla: poetry run coverage report -m
