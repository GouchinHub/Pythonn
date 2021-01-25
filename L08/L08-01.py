# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 29.10.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

import math
import random

def paaohjelma():
    print("Tämä ohjelma käyttää kirjastoja tehtävien ratkaisemiseen.")
    while True:
        valinta = valikko()
        if valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        elif valinta == 1:
            ympyran_sade()
        elif valinta == 2:
            arpaluku()
        else:
            print("Tuntematon valinta")
        print("")

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Laskea ympyrän pinta-alan")
    print("2) Arvata luvun")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    sade = int(input("Anna ympyrän säde kokonaislukuna: "))
    pinta_ala = (math.pi * (sade ** 2)) 
    print("Säteellä", sade,"ympyrän pinta-ala on", str(round(pinta_ala, 2))+".")

def arpaluku():
    print("Arvaa ohjelman arpoma kokonaisluku.")
    random.seed(37)
    oikea = random.randint(0,1000)
    kerrat = 0
    while True:
        veikkaus = int(input("Anna kokonaisluku välillä 0-1000: "))
        if veikkaus < oikea:
            print("Haettu luku on suurempi.")
            kerrat += 1
        if veikkaus > oikea:
            print("Haettu luku on pienempi.")
            kerrat += 1
        if veikkaus == oikea:
            kerrat += 1
            print("Oikein! Käytit arvaamiseen", kerrat ,"kierrosta.")
            break


paaohjelma()
