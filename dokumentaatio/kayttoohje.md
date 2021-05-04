# Käyttöohje

Lataa viimeisin versio kierrätyslistasovelluksesta. Se löytyy kohdan releases alta.

## Asennus

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

## Käyttäjän luominen ja kirjautuminen

Sovellus aukeaa näkymään, jossa on laatikot käyttäjänimelle ja salasanalle, kirjaudu sisään (login) nappula ja rekisteröidy (register) nappula. 

Jätä muut hetkeksi huomioimatta ja paina rekisteröitymis nappulaa.

Nyt aukeaa kirjautumisnäkymän kanssa lähes samanlainen rekisteröitymisnäkymä, josta puuttuu kirjaudu sisään nappula.

Valitse itsellesi käyttäjänimi ja salasana, ja kirjoita ne niille varattuihin laatikkoihin.

Paina rekisteröitymis nappulaa ja siirry takaisin kirjautumisnäkymään.

Nyt voit kirjautua sisään, tai luoda uusia käyttäjiä noudattaen edellisiä ohjeita.

## Kierrätyslistanäkymä

Kirjauduttuasi sisään näet listan eri kierrätysmateriaaleja.

Voit lisätä materiaaleja kierrätetyksi kirjoittamalla numeron sille varattuun laatikkoon ja painamalla sen vieressä olevaa nappulaa.

Sovelluksen tämänhetkisessä versiossa nappulaa painettuasi sinun täytyy kirjautua sisään uudelleen, jotta voit nähdä muutokset.

Voit kirjautua ulos painamalla kirjaudu ulos (logout) nappulaa.
