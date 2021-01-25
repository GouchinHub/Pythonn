#L05-01 Aatu

def vaihe1():
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Sopii hyvin valikon tulostamiseen.")
    return None

print("Ensimmäinen vaihe:")
print("")

vaihe1()

def vaihe2():
    luku = int(input("Anna luku: "))
    print("Päätasolla: ", luku)
    print("Aliohjelmassa:", luku)
    print("Aliohjelmassa luvun neliö:", luku ** 2 )
    print("Päätasolla aliohjelman jälkeen: ",luku)
    return None

print("")
print("Toinen vaihe:")

vaihe2()

def vaihe3():
    enimi = input("Anna etunimi: ")
    snimi = input("Anna sukunimi: ")
    print("Etunimi '"+ enimi +"' ja sukunimi '"+ snimi +"' muodostavat nimen '"+enimi, snimi+"'.")
    return None

print("")
print("Kolmas vaihe:")

vaihe3()

print("Kiitos ohjelman käytöstä.")
