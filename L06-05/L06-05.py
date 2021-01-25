#L06-05 Aatu

def paaohjelma():
    #tiedosto = input("Anna päivittäiset askeltiedot sisältävän tiedoston nimi: ")
    #tiedosto = ("testlines.txt")
    tiedosto = ("2017Fitbit.txt")
    print("Tämä ohjelma laskee tunnuslukuja askeltietomääristä.")
    while True:
        askeltiedot = open(tiedosto, 'r')
        print("Mitä haluat selvittää tiedostossa olevista askelmäärätiedoista:")
        print("1) Laske koko vuoden askelmäärä")
        print("2) Selvitä suurin päivittäinen askelmäärä")
        print("3) Tallenna yhteenvetotiedot")
        print("0) Lopeta")
        valinta = int(input("Valintasi: "))
        if valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        elif valinta == 1:
            koko_vuosi(askeltiedot)
            print("Koko vuoden tulos oli",summa,"askelta.")
        elif valinta == 2:
            suurin_askelmaara(askeltiedot)
            print("Suurin päivittäinen askelmäärä oli",suurin,"askelta.")
        elif valinta == 3:
            yhteenveto()
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
        print("")
            


def koko_vuosi(askeltiedot):
    global summa
    summa = 0
    while True:
        rivi = askeltiedot.readline()
        linefix = rivi[:-1]
        nums = linefix.split(';')
        if len(rivi) == 0:
            break
        
        for alkio in nums[2::9]:
            summa += int(alkio)
    askeltiedot.close()
    
    return summa

def suurin_askelmaara(askeltiedot):
    global suurin
    suurin = 0
    while True:
        rivi = askeltiedot.readline()
        linefix = rivi[:-1]
        nums = linefix.split(';')
        if len(rivi) == 0:
            break
        
        for alkio in nums[2::9]:
            if int(suurin) < int(alkio):
                suurin = alkio
    askeltiedot.close()
    return suurin
    
    
    

def yhteenveto():
    global suurin
    global summa
    string = str(summa)
    rivi1 = str("Suurin päivittäinen askelmäärä oli")
    rivi3 = str("askelta.")
    rivi2 = str("ja koko vuoden askelmäärä oli")
    tiedosto2 = input("Anna tulostieto-tiedoston nimi: ")
    tallennus = open(tiedosto2, 'w')
    
    tallennus.write(rivi1 + ' ')
    tallennus.write(suurin + ' ')
    tallennus.write(rivi3 + '\n')
    tallennus.write(rivi2 + ' ')
    tallennus.write(string + ' ')
    tallennus.write(rivi3 + '\n')
    
    tallennus.close()

paaohjelma()
