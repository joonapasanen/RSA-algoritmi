# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

![alt text](![alt text](kuvat/kattavuusraportti.png))

## Mitä on testattu ja minkälaisilla syötteillä

### Yksikkötestit

Satunnaisten parittomien lukujen luonti väliltä [2^1023, 2^1024) (funktio sample_odd_number primes.py moduulista). Yksikkötestit testaavat että luku on pariton, sekä että luku kuuluu halutulle intervallille. Funktion toimivuus testataan lisäämällä sata sen luomaa numeroa listaan ja tarkistamalla jokaiselle numerolle listalla, että yllä mainitut testit läpäisevät.

Sieve of Eratosthenes -algoritmin toiminta (primes.py moduulista). Yksikkötestit testaavat että algoritmi löytää kaikki alkuluvut, jotka ovat pienempiä tai yhtäsuuria kuin 100 ja 500, algoritmin palauttamaa tulosta verrataan sitten oikeaan listaan alkuluvuista näiden rajojen alapuolelta. Valitut rajat ovat edustavia algoritmin käyttötarkoitukseen. Tämän lisäksi testataan, että syötteet jotka ovat pienempiä kuin 2 palauttavat tyhjän listan, sillä 2 on pienin alkuluku. Tätä testataan syötteillä 1 ja -21.

## Miten testit voi toistaa?

Testit voi suorittaa komennolla: poetry run coverage run --branch -m pytest

Ja tulostaa konsoliin komennolla: poetry run coverage report -m
