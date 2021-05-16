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
3. Anna sovelluksen adminkäyttäjälle salasana


4. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

## Käyttäjän luominen ja kirjautuminen

Sovelluksen avattuasi paina register näppäintä ja valitse itsellesi käyttäjätunnus (username) ja salasana (password)

Kirjoita käyttäjätunnus ja salasana niille varattuihin laatikoihin.

Huomaa, että sinun täytyy kirjoittaa sama salasana kahdesti.

Paina rekisteröitymisnäppäintä, jonka jälkeen voit kirjautua sisään kirjoittamalla valitsemasi käyttäjänimen ja salasanan kirjautumissivulla.

## Kierrätyslistanäkymä

Kirjauduttuasi sisään näet listan eri kierrätysmateriaaleja.

Voit lisätä materiaaleja kierrätetyksi kirjoittamalla numeron sille varattuun laatikkoon ja painamalla sen vieressä olevaa nappulaa.

Voit kirjautua ulos painamalla kirjaudu ulos (logout) nappulaa.

## Adminkäyttäjä

Jos valitset kirjautumissivulla kirjaudu admin käyttäjällä näppäimen, sinut ohjataan sivulle, jolle voit kirjoittaa sovelluksen alustuksessa asettamasi salasanan.

Kirjauduttuasi sisään voit painaa näytä käyttäjät painiketta, näytä tilastot painiketta, tai molempia.

Käyttäjiä voi poistaa painamalla käyttäjän nimen päältä.
