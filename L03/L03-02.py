#L03-02 aatu

x = str(input("Haluatko lopettaa ohjelman suorittamisen (k/K): "))

if(x == 'K')or(x == 'k'):
    print("Kiitos ohjelman käytöstä.")
else:
    N = input("Anna nimi: ")
    PW = input("Anna salasana: ")
    if(N == 'Matti')and(PW == 'salasana'):
        print("Käyttäjä tunnistettu.")
    else:
        print("Antamasi nimi oli", len(N),"merkkiä pitkä, mutta se tai salasana ei ollut oikein.")
