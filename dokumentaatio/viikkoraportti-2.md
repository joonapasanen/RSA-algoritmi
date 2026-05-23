# Viikkoraportti 2

Käytin tällä viikolla noin 12 tuntia työskentelyyn.

1. Mitä olen tehnyt tällä viikolla?

Tällä viikolla olen opiskellut miten alkulukujen luonti käytännössä toimii käyttäen Miller-Rabin-testiä ja kirjoittanut siitä oman toteutuksen, sekä alustavat yksikkötestit. Tein myös saman kahdelle muulle funktiolle, jotka ovat tärkeitä oikean pituisten alkulukujen etsinnässä algoritmia varten. Nämä ovat parittomien, 1024-bittisten lukujen generointi ja Eratostheneen seula, jota käytetään pienten alkulukujen etsintään jonkin kokonaisluku rajan alta.

2. Miten ohjelma on edistynyt?

Algoritmin ensimmäinen osa eli sopivien suurten alkulukujen etsintä alkaa käytännössä olla valmis, kaikki osat toimivat itsekseen halutulla tavalla, mutta minun tulee vielä tarkastella niiden tehokkuutta, kun niitä käytetään yhdessä. Olen tämän lisäksi kirjoittanut alustavat yksikkötestit kaikille funktioille joiden parissa olen työskennellyt.

3. Mitä opin tällä viikolla / tänään?

Perehdyin tällä viikolla tarkemmin suurten alkulukujen luontiin tarkemmin. Tutustuin Miller-Rabin-testin matemaattisiin perusteisiin hieman tarkemmin ja ymmärrän nyt miten se johtaa juurensa Fermat'n alkuluku testistä ja modulaarisen aritmetiikaan liittyvistä faktoista. Tämän lisäksi tutustuin siihen miten Pytest toimii ja miten sillä kirjoitetaan yksikkötestejä, sillä minulla ei ollut tästä aiempaa kokemusta.

4. Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Yksi asia johon tarvitsin selvennyksen on, että saako projektissa käyttää Pythonin standardikirjaston moduuleja (secrets ja random) satunnaisten lukujen luontiin?

5. Mitä teen seuraavaksi?

Nyt kun suurten alkulukujen satunnainen luonti onnistuu, seuraavaksi siirryn RSA-algoritmin pääosan, eli avainten luonnin, kehittämisen pariin.
