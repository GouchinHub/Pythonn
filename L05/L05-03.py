#05-03 Aatu
def funktio(luku):
    for i in range(0, luku):
        print(teksti)
    print("")
teksti = input("Anna teksti: ")
if (teksti == 'lopeta'):
    print("Lopetetaan.")
    print("Kiitos ohjelman käytöstä.")
else:
    luku = int(input("Anna luku: "))
    while True:
        funktio(luku)
        teksti = input("Anna teksti: ")
        if (teksti == 'lopeta'):
            print("Lopetetaan.")
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            luku = int(input("Anna luku: "))
                
