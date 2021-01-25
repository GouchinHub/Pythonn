# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 3.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

class DATA():
    rivit = 0
    luku = 0
    
def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def Lue_tiedosto(tiedosto):
    data = DATA()
    luvut = []
    while True:
        rivi = tiedosto.readline()
        if len(rivi) == 0:
            break
        data.rivit += 1
        sarakkeet = rivi[:-1].split(";")
        luvut.append(sarakkeet[1])
        data.luku = luvut
    tiedosto.close()
    return data

def Analysoi(data):
    lista = []
    for L in data.luku:
        lista.append(int(L))
    total = 0
    for i in lista:
        total += i
        yield total

def Tallenna(tiedosto2, acclist):
    lista = acclist
    for i in range(len(acclist)):
        tiedosto2.write(str(acclist[i])+";")
    tiedosto2.write("\n")
    tiedosto2.close
    
        
        
