# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 15.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

import sys

def paaohjelma():
    lista = tietojen_siivous()
    esitysmuodon_standarointi(lista)
    print("Kiitos ohjelman käytöstä.")
    sys.exit(0)

def tietojen_siivous():
    nimi = input("Anna luettavan tiedoston nimi: ")
    hyvaksytyt = []
    luetut = 0
    poistetut = 0
    try:
        tiedosto = open(nimi, 'r')
    except OSError:
        print("Tiedoston '{0:s}' avaaminen epäonnistui.".format(nimi))
        sys.exit(0)
    while True:
        rivi = tiedosto.readline()
        luetut += 1
        if rivi[:-1].isalpha() == True:
            hyvaksytyt.append(rivi[:-1])
        else:
            poistetut += 1
        if len(rivi) == 0:
            break
    print("Luettiin {0:d} riviä tiedostosta '{1:s}'.".format(luetut,nimi))
    print("Hylättiin",poistetut,"riviä.")
    return hyvaksytyt

def esitysmuodon_standarointi(lista):
    nimi = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitetut = 0
    try:
        tiedosto = open(nimi, 'w')
    except OSError:
        print("Tiedoston '{0:s}' avaaminen epäonnistui.".format(nimi))
        sys.exit(0)
    for alkio in lista:
        tiedosto.write(alkio.lower()+"\n")
        kirjoitetut += 1
    tiedosto.close()
    print("Kirjoitettiin {0:d} riviä tiedostoon '{1:s}'.".format(kirjoitetut ,nimi))
    return None
    
    

paaohjelma()
            
            
        
