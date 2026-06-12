# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma koostuu 3 moduulista; primes.py jota käytetään alkulukujen luontiin, rsa.py joka sisältää RSA-algoritmin avainten luonnin sekä apumetodit jotka eivät liity alkulukujen luontiin, sekä main.py joka sisältää konsolipohjaisen käyttöliittymän. Ohjelmaa kutsutaan main.py moduulista, joka avaa käyttöliittymän.

## Saavutetut aika- ja tilavaativuudet

Ohjelman metodien implementaatio vastaavat wikipediasta löytyviä pseudokoodi versioita. Listaan aika- ja tilavaativuudet alle:

- Sieve of Eratosthenes: aikavaativuus on O(n loglog(n)) ja tilavaativuus on O(n).

- Miller-Rabin: aikatilavuus on O(k\*n^3), jossa k on kierrosten määrä ja n syötteen pituus numeroina. Tilavaativuus on O(log(n)), jossa n on bittien määrä.

- Laajenettu Eukleideen Algoritmi: aikatilavuus on O(log(min(a,b))) ja tilavaativuus on vakio O(1).

## Työn mahdolliset puutteet ja parannusehdotukset

Työstä puuttuu joitain asioita (ohjeiden mukaisesti), joita löytyisi oikeasta RSA implementaatiosta, esimerkiksi padding olisi varmasti yksi tälläinen asia. Näiden asioiden implementaatio varmasti parantaisi projektia, mutta toisaalta työmäärä saattaisi nousta liian suureksi.

## Laajojen kielimallien käyttö

Olen käyttänyt ChatGPT:tä ja Claudea selittämään eri konsepteja, esim. algoritmiin liittyvästä matematiikasta. Tämän lisäksi olen käyttänyt kielimalleja selittämään esim. vertaisarvioinissa olevien metodien toimintaa, jos jokin on ollut epäselvää ja myös etsimään lähteitä joista voin esim. löytää suuria alkulukuja.

## Käytetyt lähteet

- https://en.wikipedia.org/wiki/RSA_cryptosystem
- https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
- https://en.wikipedia.org/wiki/Euclidean_algorithm
- https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
- https://cp-algorithms.com/algebra/extended-euclid-algorithm.html
- https://factordb.com
