#L07-04 Aatu

def paaohjelma():
    print("Tämä ohjelma laskee töihin käytetyn ajan.")
    class TYOPAIVA:
        tyotunti = ""
    tyotunnit = []
    ali_ohjelma(tyotunnit)
    tulostus_ohjelma(tyotunnit)
    

def ali_ohjelma(tyotunnit):
    paiva = int(input("Kuinka monen päivän tiedot haluat syöttää: "))
    for i in range(1, paiva+1):
        print("Anna", str(i)+". päivän", end=" ")
        tunnit = float(input("työtunnit: "))
        tyotunnit.append(tunnit)

def tulostus_ohjelma(tyotunnit):
    print("Syötit seuraavat tunnit:", end=" ")
    for h in range(0, len(tyotunnit)):
        print (str(tyotunnit[h])+"h,", end=" ")
    print("yhteensä", round(sum(tyotunnit),2) ,"tuntia.")
    keskimaara = round(float(sum(tyotunnit)) / len(tyotunnit),2)
    print("Keskimääräisen työpäivän pituus oli", str(keskimaara) +"h.")
                       
paaohjelma()
