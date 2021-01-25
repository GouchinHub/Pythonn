# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 16.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

import sys

def paaohjelma():
    sanakirja = tietojen_jarjestelu()
    tietojen_kirjaus(sanakirja)
    print("Kiitos ohjelman käytöstä.")
    sys.exit(0)

def tietojen_jarjestelu():
    nimi = input("Anna luettavan tiedoston nimi: ")
    lista = []
    sanakirja = {}
    try:
        tiedosto = open(nimi, 'r')
    except OSError:
        print("Tiedoston '{0:s}' avaaminen epäonnistui.".format(nimi))
        sys.exit(0)
    while True:
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            break
        lista.append(rivi[:-1])
    for alkio in lista:
        if alkio not in sanakirja:
            sanakirja[str(alkio)] = 1
        else:
            if sanakirja[str(alkio)] >= 1:
                sanakirja[str(alkio)] += 1
    return sanakirja
    

def tietojen_kirjaus(sanakirja):
    nimi = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        tiedosto = open(nimi, 'w')
    except OSError:
        print("Tiedoston '{0:s}' avaaminen epäonnistui.".format(nimi))
        sys.exit(0)
    lajiteltu = sorted(sanakirja.items(), key=lambda sanakirja:sanakirja[0])
    for alkio in lajiteltu:
        print("{0} {1}".format(alkio[0], alkio[1]))
    for alkio in lajiteltu:
        tiedosto.write("{0} {1}\n".format(alkio[0], alkio[1]))
    tiedosto.close()
    return None
    
    
paaohjelma()
            
            
        
