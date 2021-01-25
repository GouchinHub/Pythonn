#L07-05 Aatu
class AUTOKAUPPA():
        auto = ""
        hinta = 0
        
def paaohjelma():
    autot = []
    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    while True:
        print("Käytettävissä olevat toiminnot:")
        print("1) Anna auton tiedot")
        print("2) Tulosta autojen tiedot")
        print("0) Lopeta")
        valinta = int(input("Valintasi: "))
        if valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        elif valinta == 1:
            tiedot(autot)
        elif valinta == 2:
            tulostus(autot)
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print("")

def tiedot(lista):
    myynti = AUTOKAUPPA()
    myynti.auto = input("Anna auton merkki: ")
    myynti.hinta = int(input("Anna auton hinta: "))
    lista.append(myynti)
    return lista

def tulostus(lista):
    print("Listalta löytyy seuraavat automerkit ja hinnat:")
    for myynti in lista:
        print(myynti.auto, myynti.hinta)
    return lista



paaohjelma()
        

