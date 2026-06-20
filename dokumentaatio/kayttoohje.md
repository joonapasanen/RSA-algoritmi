# Käyttöohje

## Käyttöliittymä

Ohjelman käyttöliittymä avataan komennolla:

`python src/main.py`

Tämä avaa käyttöliittymän terminaaliin.

## Ohjelman toiminta

Ohjelman käynnistyessä käyttäjän tulee kopioida terminaaliin ilmestyvä yksityinen avain, ylimääräisistä välilyönneistä ei tarvitse huolehtia. Tämän jälkeen käyttäjä voi jatkaa eteenpäin painamalla enteriä.

Ohjelmassa on kaksi päätoimintoa, syöttämällä kirjaimen 's' (send) voi lisätä viestejä jonoon, jotka salataan julkisella avaimella. Syöttämällä kirjaimen 'r' (receive) voi taas lukea viestejä jonosta, mutta tämä vaatii ohjelman alussa näytetyn yksityisen avaimen tai muuten viestin lukeminen epäonnistuu.
