# Sovelluksen tämänhetkinen tila

Sovelluksessa voi tällä hetkellä luoda käyttäjän ja kirjautua sisään. Sisäänkirjautumisen jälkeen näkyy käyttäjäkohtainen listanäkymä, jossa on eri kierrätysmateriaaleja. Materiaalien määrää voi lisätä. Materiaaleista puuttuu tällä hetkellä yksiköt. Virheilmoitukset eivät ole vielä paikallaan, jonka takia sovellus jäätyy ja täytyy käynnistää uudelleen aina, jos tekee virheen, esim. syöttää väärän käyttäjänimen tai salasanan. Testit eivät ole tällä hetkellä toiminnassa, koska pytest ei löydä entities kansiota.

# Dokumentaatio

[Vaativuusmäärittely](https://github.com/JuhahuJ/ot-harjoitustyo/blob/master/dokumentaatio/vaativuusmaarittely.md)

[Tuntikirjanpito](https://github.com/JuhahuJ/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

# Asennus

1. Asenna poetry komennolla:
```bash
poetry install
```
2. Alusta sovellus komennolla:
```bash
poetry run invoke build
```
3. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```
# Sovelluksen normaali käynnistys

Sovellus käynnistyy kohdan 3 komennolla
