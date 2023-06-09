Pràctica de LP:
Aquesta [pàgina](https://gebakx.github.io/lp-achurch-23/) descriu la pràctica de GEI-LP (edició 2022-2023 Q2). La vostra feina consisteix en implementar un petit intèrpret de λ-càlcul anomenat AChurch.

Per poder executar en local serà necessari descarregar els fitxers i seguidament instal·lar les dependències:
```
git clone https://github.com/miquelt9/LP-FIB/
cd LP-FIB/AChurch
pip install -r requirements.txt
```

A continuació caldrà compilar la gramàtica amb:
```
antlr4 -Dlanguage=Python3 -no-listener -visitor lc.g4 
```
I (potser) haurem d'assegurar-nos de tenir un _environment_ configurat correctmanet, el que es troba a la carpeta es pot utlitzar fent:
```
source venv/bin/activate
```
Finalment només caldrà executar el bot:
```
python3 achurch.py
```
Compte! És possible que doni error quan l'executis donat que el programa buscarà un fitxer `token.txt`, el qual fa referència al bot de telegram. Pots crear el teu propi bot a bé fer les proves que vulguis al ja disponible ([Bot Telegram](https://t.me/lambda_calcul_bot))
