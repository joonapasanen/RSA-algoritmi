# Projektin määrittelydokumentti

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)

## Tekninen toteutus

Toteutan harjoitustyössä [RSA-algoritmin](https://en.wikipedia.org/wiki/RSA_cryptosystem) Pythonilla. Harjoitustyön ydin on salausalgorimit. Tarkemmin ratkaistava ongelma on tekstimuotoisten viestien turvallinen lähettäminen ja vastaanottaminen. Ratkaisu perustuu RSA:n epäsymmetriseen salaukseen, jossa käytetään julkisen ja yksityisen avaimen muodostamaa avainparia.

### Algoritmit ja tietorakenteet

RSA:n toteuttaminen vaatii useiden eri algoritmien toteuttamista:

- Miller-Rabin-testi (myös Miller-Rabin-algoritmi), jolla testataan onko jokin luku todennäköisesti alkuluku.
- Eratostheneen seula, jota käytetään pienten alkulukujen luontiin.
- Laajennettu Eukleideen algoritmi, jota käytetään salauksessa tarvittavien eksponenttien luomiseen.

### Tavoitteena olevat aika- ja tilavaativuudet

Miller-Rabin-testin aikavaativuus on [O(k \* n^3)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Complexity), jossa k merkitsee testien ajamiseen käytettävää kierrosten määrä ja n syöteen pituutta biteissä. Tilavaativuus taas on O(log(n)), koska algoritmi säilyttää vain syöteen ja muutamia apumuuttujia.

[Eratostheneen seulan](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithmic_complexity) aikavaativuus on [O(n * log(log(n)))] ja tilavaativuus on O(n), jossa n merkitsee lukua jota pienemmät alkuluvut algoritmi laskee.

Laajennetun Eukleideen algoritmin [aikavaativuus ja tilavaativuus](https://www.geeksforgeeks.org/dsa/euclidean-algorithms-basic-and-extended) ovat O(log min(a, b)), jossa a ja b ovat luvut joiden suurinta yhteistä tekijää etsitään.

Nämä ovat siis aika- ja tilavuustavoitteet joihin itsekin pyrin.

## Ohjelman toiminta

Ohjelma ottaa syötteenä vastaan lähettäjän, vastaanottajan ja lähetettävän viestin. Ensin ohjelman tulee tarkastaa onko vastaanottajalla olemassa yksityistä ja julkista avainta, sekä tarvittaessa luoda ja tallentaa ne. Sen jälkeen lähettäjä salaa viestin käyttäen vastaanottajan julkista avainta. Tämän jälkeen vastaanottaja voi purkaa salauksen käyttämällä omaa yksityistä avaintaan.

## Kielet ja vertaisarviointi

Pythonin lisäksi pystyn vertaisarvioimaan projekteja jotka on tehty TypeScriptillä ja C:llä.

## Lähteet

Käytän harjoitustyössä lähteinä:

- https://en.wikipedia.org/wiki/RSA_cryptosystem
- https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
- https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
- https://www.geeksforgeeks.org/dsa/euclidean-algorithms-basic-and-extended
