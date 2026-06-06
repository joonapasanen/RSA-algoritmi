# Testausdokumentti

## Yksikkötestauksen kattavuusraportti

![](kuvat/kattavuusraportti.png)

## Mitä on testattu ja minkälaisilla syötteillä

### Yksikkötestit

Satunnaisten parittomien lukujen luonti väliltä [2^1023, 2^1024) (funktio sample_odd_number primes.py moduulista). Yksikkötestit testaavat että luku on pariton, sekä että luku kuuluu halutulle intervallille. Funktion toimivuus testataan lisäämällä sata sen luomaa numeroa listaan ja tarkistamalla jokaiselle numerolle listalla, että yllä mainitut testit läpäisevät.

Sieve of Eratosthenes -algoritmin toiminta (primes.py moduulista). Yksikkötestit testaavat että algoritmi löytää kaikki alkuluvut, jotka ovat pienempiä tai yhtäsuuria kuin 100 ja 500, algoritmin palauttamaa tulosta verrataan sitten oikeaan listaan alkuluvuista näiden rajojen alapuolelta. Valitut rajat ovat edustavia algoritmin käyttötarkoitukseen. Tämän lisäksi testataan, että syötteet jotka ovat pienempiä kuin 2 palauttavat tyhjän listan, sillä 2 on pienin alkuluku. Tätä testataan syötteillä 1 ja -21.

Miller-Rabin-testin toiminta (primes.py moduulista). Miller-Rabin-testin yksikkötestit testaavat, että testi osaa tunnistaa alkuluvut, komposiittiluvut, sekä Carmichaelin luvut, jotka ovat joukko komposiittilukuja, jotka kuitenkin huijaavat yksinkertaisemmat alkulukutestit kuten Fermat'n testin. Käytän jokaisessa kategoriassa syötteinä kolmea eri lukua, joista yksi on pieni luku ja kaksi suuria 1024 bittisiä lukuja, joiden on tarkoitus edustaa syötteitä joita algoritmi ottaa vastaan RSA-algoritmia käyttäessä. Miller-Rabin on pohjimmiltaan stokastinen testi, mutta kun kierrosten määrä on 15 (joka se on automaattisesti toteutuksessa) niin todennäköisyys että algoritmi palauttaa väärän vastauksen on 1 - 0.999999999 eli noin 1 kerran miljardista. Tämän perusteella testi toimii käytännössä determinisesti.

## Miten testit voi toistaa?

Testit voi suorittaa komennolla: poetry run coverage run --branch -m pytest

Ja tulostaa konsoliin komennolla: poetry run coverage report -m
