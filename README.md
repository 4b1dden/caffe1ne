# caffe1ne
### *work in progress*

Projekt zameraný na integráciu vnoreného systému do (zatiaľ) kávovara na každodenné použitie. Pri vývoji bolo používané Raspberry Pi 3. V koreňovej zložke projektu sa nachádzajú tri zložky a súbor.
 - api
 - substrate
 - web_interface
 - init.sh

V zložke ```api``` sa nachádza api projektu - Flask aplikácia. Poskytuje dáta pre kontrolný panel, otvára endpointy pre zarobenie kávy a ukladá štatistiky do databázy.
```substrate``` slúži pre uloženie všetkého zdrojového kódu, ktorý je potreba ku komunikácii vnoreného systému s kávovarom.
Vo ```web_interface``` je Vue.js aplikácia, ktorá slúži ako ovládací panel a nástroj na sledovanie štatistík.

## Inštalácia
```
chmod +x init.sh
./init.sh
```
Nakonfiguruje všetky projekty a spustí požadované servery (api, webové rozhranie). Po úspešnom spustení sú servery prístupné na lokálnej IP vnoreného systému, aby medzi sebou mohli komunikovať.
