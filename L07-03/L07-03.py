#07-03 Aatu
def paaohjelma():
    tiedosto = open("marjoja.txt", "r")
    poistettava_rivi = tiedosto.readline()
    ajoitus = []
    marja = []
    lukumaara = 0
    
    while True:
        rivi = tiedosto.readline()
        linefix = rivi[:-1]
        data = linefix.split(";")
        lukumaara += 1
        if len(rivi) == 0:
            break
        for alkio in data[2::2]:
            ajoitus += [alkio]
        for alkio2 in data[0::3]:
            marja += [alkio2]

    for i in range(lukumaara - 1):
        print("Kello oli",str(ajoitus[i])+", kun punnittiin marjoja",str(marja[i])+".")
    

    tiedosto.close()

paaohjelma()
