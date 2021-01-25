# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 31.10.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

def paaohjelma():
    import L08_T3Kirjasto
    print("Käytetään lämpötilamuunnoskirjaston versiota", L08_T3Kirjasto.versio )
    while True:
        valinta = valikko()
        if valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        if 1 <= valinta <= 6:
            Lampotila = float(input("Anna lähtölämpötila: "))
            if valinta == 1:
                muunnettu = L08_T3Kirjasto.Celsius_Fahrenheit(Lampotila)
                print("Lämpötila Fahrenheit asteina:", round(muunnettu,2))
            elif valinta == 2:
                muunnettu = L08_T3Kirjasto.Celsius_Kelvin(Lampotila)
                print("Lämpötila Kelvin asteina:", round(muunnettu,2))
            elif valinta == 3:
                muunnettu = L08_T3Kirjasto.Fahrenheit_Kelvin(Lampotila)
                print("Lämpötila Kelvin asteina:", round(muunnettu,2))
            elif valinta == 4:
                muunnettu = L08_T3Kirjasto.Fahrenheit_Celsius(Lampotila)
                print("Lämpötila Celsius asteina:", round(muunnettu,2))
            elif valinta == 5:
                muunnettu = L08_T3Kirjasto.Kelvin_Celsius(Lampotila)
                print("Lämpötila Celsius asteina:", round(muunnettu,2))
            elif valinta == 6:
                muunnettu = L08_T3Kirjasto.Kelvin_Fahrenheit(Lampotila)
                print("Lämpötila Fahrenheit asteina:", round(muunnettu,2))
        else:
            print("Tuntematon valinta")
        print("")

def valikko():
    print("Minkä lämpötilamuunnoksen haluat tehdä?")
    print("1) Celsius->Fahrenheit")
    print("2) Celsius->Kelvin")
    print("3) Fahrenheit->Kelvin")
    print("4) Fahrenheit->Celsius")
    print("5) Kelvin->Celsius")
    print("6) Kelvin->Fahrenheit")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta


paaohjelma()
