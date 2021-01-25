#05-05 Aatu

##Pääohjelma toteuttaa ohjelmaa kunnes sen lopetus on määrätty

def paaohlelma():
    print("Tämä ohjelma tulostaa sanan käyttäjän haluamalla tavalla.")
    while True:
        valinta = ohjelma_1()
        if valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        elif valinta == 1:
            sana = str(input("Anna sana: "))
            ohjelma_2(valinta, sana)
        elif valinta == 2:
            ohjelma_2(valinta, sana)
        elif valinta == 3:
            ohjelma_2(valinta, sana)       
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
            print("")

## Tämä ohjelma tulostaa valikon ja kysyy valinnan
def ohjelma_1():
    print("Käytettävissä olevat toiminnot:")
    print("1) Määritä sana")
    print("2) Tulosta sana alusta loppuun")
    print("3) Tulosta sana lopusta alkuun")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

## Tämä ohjelma tulostaa annetun sanan halutulla tavalla
def ohjelma_2(valinta, sana):
    if (valinta == 1):
        print("")
        return sana
    elif (valinta == 2):
        pituus = len(sana)
        for i in range(0, pituus):
            pituus -= 1
            print(sana [-(pituus +1):])
        print("")
        return sana
    elif (valinta == 3):
        k_sana = sana[::-1]
        pituus = len(sana)
        for i in range(0, pituus):
            pituus -= 1
            print(k_sana [-(pituus +1):])
        print("")
        return sana    
            

paaohlelma()
