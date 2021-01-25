# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 3.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

import L08_T5Kirjasto

def paaohjelma():
    acclist = []
    while True:
        valinta = L08_T5Kirjasto.valikko()
        if valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        elif valinta == 1:
            tiedosto = open("L08T5Data.txt", "r")
            data = L08_T5Kirjasto.Lue_tiedosto(tiedosto)
            print("Tiedosto 'L08T5Data.txt' luettu,",data.rivit,"riviä.")
        elif valinta == 2:
            acclist = list(L08_T5Kirjasto.Analysoi(data))
            accsum = sum(acclist)
            print("Tiedot analysoitu, arvot yhteensä",str(accsum)+".")
        elif valinta == 3:
            tiedosto2 = open("L08T5Tulos.txt", "w")
            L08_T5Kirjasto.Tallenna(tiedosto2, acclist)
            print("Tulokset tallennettu tiedostoon 'L08T5Tulos.txt'.")
        else:
            print("Tuntematon valinta")
        print("")


paaohjelma()



