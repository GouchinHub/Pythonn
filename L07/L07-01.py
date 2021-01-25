#07-01 Aatu

def kauppalistaohjelma():
    ostoslista = []
    while True:
        print("Ostoslistasi sisältää seuraavat tuotteet:")
        print(ostoslista)
        print("Voit valita alla olevista toiminnoista:")
        print("1) Lisää")
        print("2) Poista")
        print("0) Lopeta")
        valinta = int(input("Valintasi: "))
        if valinta == 0:
            print("Sinulta jäi ostamatta seuraavat tuotteet:")
            print(ostoslista)
            print("Kiitos ohjelman käytöstä.")
            break
        if valinta == 1:
            tuote = input("Anna lisättävä tuote: ")
            ostoslista.append(tuote)
        elif valinta == 2:
            print("Ostoslistassasi on", len(ostoslista) , "tuotetta.")
            poisto = int(input("Anna poistettavan tuotteen järjestysnumero: "))
            del ostoslista[(poisto - 1)]
        else:
            print("Tunnistamaton valinta.")
        print("")
            
        
kauppalistaohjelma()
