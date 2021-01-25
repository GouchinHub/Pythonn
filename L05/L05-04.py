#L05-04

def tarkistava_ohjelma():
    x = kysyva_ohjelma()
    if 5 > x:
        print("Liian lyhyt,", x,"merkkiä, anna uusi.")
        return tarkistava_ohjelma()
    elif 15 < x:
        print("Liian pitkä,", x,"merkkiä, anna uusi.")
        return tarkistava_ohjelma()
    else:
        print("Annoit sopivan merkkijonon,", x,"merkkiä.")
        print("Kiitos ohjelman käytöstä.")
        sopiva = x
        return sopiva

def kysyva_ohjelma():
    mjono = str(input("Anna merkkijono, 5-15 merkkiä: "))
    arvo = len(mjono)
    return arvo
       
def paaohjelma():
    tarkistava_ohjelma()
    
    
paaohjelma()
