# Kierrätyslistasovellus

Sovelluksen avulla voi pitää yllä sitä, kuinka paljon on kierrättäny. Sovellusta voi käyttää usea käyttäjä, joilla on oma lista. Adminkäyttäjällä voi poistaa muita käyttäjiä ja tarkastella sitä, kuinka paljon kaikki ovat kierrättäneet yhteensä.

# Dokumentaatio

[Vaativuusmäärittely](https://github.com/JuhahuJ/ot-harjoitustyo/blob/master/dokumentaatio/vaativuusmaarittely.md)

[Tuntikirjanpito](https://github.com/JuhahuJ/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Ohjeet](https://github.com/JuhahuJ/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Arkkitehtuuri](https://github.com/JuhahuJ/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testaus](https://github.com/JuhahuJ/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

# Asennus

1. Asenna poetry komennolla:
```bash
poetry install
```
2. Alusta sovellus komennolla:
```bash
poetry run invoke build
```
3. Anna sovellukselle valitsemasi admin salasana jota käytetään admin menuun kirjautumiseen

4. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```
# Sovelluksen normaali käynnistys

Sovellus käynnistyy kohdan 4 komennolla

# Muita sovelluksessa suoritettavia komentoja

Testikattavuusraportin generoiminen htmlcov hakemiston sisälle:
```bash
poetry run invoke coverage-report
```
Raportin generoiminen suorittaa myös testit, jotka voi toki suorittaa myös komennolla:
```bash
poetry run invoke test
```
Pylintin tarkastukset voi suorittaa komennolla:
```bash
poetry run invoke lint
```
