# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 29.10.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

import datetime

def paaohjelma():
    datetime.datetime
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    while True:
        valinta = valikko()
        if valinta == 0:
            print("Kiitos ohjelman käytöstä")
            break
        elif valinta == 1:
            komponentit()
        elif valinta == 2:
            arpaluku()
        elif valinta == 3:
            kek
        elif valinta == 4:
            kek2
        else:
            print("Tuntematon valinta")
        print("")

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Tunnistaa aika-olion komponentit:")
    print("2) Laskea iän päivinä")
    print("3) Tulostaa viikonpäivät")
    print("4) Tulostaa kuukaudet")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def komponentit():
    lista = []
    pvm = ('24.12.2012 20:13')
    #pvm = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    
    print(fix)

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
            print("Oikein! Käytit arvaamiseen", kerrat ,"kierrosta.")
            break


paaohjelma()
