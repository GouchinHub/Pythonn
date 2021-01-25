# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 18.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: https://stackoverflow.com/

import sys
import HT_kirjasto as krj

def paaohjelma():
    nimijavuosi = []
    tiedot = []         #nimetään käytettävät listat
    data = []
    lippu = True        #määritellään lippu
    while True:
        valinta = krj.valikko()
        if valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            sys.exit(0)
        if valinta == 1:
            nimijavuosi = krj.havainto_vuosi()
        elif valinta == 2:
            tiedot = krj.lue_tiedosto(nimijavuosi)
        elif valinta == 3:
            data = krj.paivittainen_analysointi(tiedot)
        elif valinta == 4:
            krj.paivittainen_tallennus(data,nimijavuosi)
        elif valinta == 5:
            tiedot = krj.ilmatieteen_laitos(nimijavuosi)
        elif valinta == 6:
            data = krj.kuukausittainen_analysointi(tiedot,)

        elif valinta == 7:
            lippu = krj.kuukausittainen_tallennus(data,nimijavuosi,lippu)
        elif valinta == 8:
            data = krj.tuntikohtainen_analysointi(tiedot)
        elif valinta == 9:
            krj.tuntikohtainen_kirjoitus(data, nimijavuosi)
        print()

paaohjelma()

##################################################################################################
#eof
