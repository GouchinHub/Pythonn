# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 7.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

import sys

def paaohjelma():
    parametri = "10.0"
    aliohjelma(parametri)
    parametri = "abc"
    aliohjelma(parametri)

def aliohjelma(parametri):   
    print("Aliohjelman parametrina tuli",str(parametri))
    rivimaara = 0
    try:
        tnimi = input("Anna tiedostonimi: ")
        tiedosto = open(tnimi, 'r')
    except OSError:
        print("Tiedoston '{0:s}' avaaminen epäonnistui.".format(tnimi))
        sys.exit(0)
    while True:
        try:
            rivi = tiedosto.readline()
            rivimaara += 1
            if len(rivi) == 0:
                break
            try:
                parametri = float(parametri)
            except ValueError:
                print("Rivi",str(rivimaara)+": Parametri oli väärää tietotyyppiä.")
                sys.exit(0)
            alkiot = rivi[:-1].split(";")
            x = float(alkiot[0]) / float(alkiot[1])
            y = parametri + x
            print("Rivi",str(rivimaara)+": Summa on {0:.2f}.".format(float(y)))
        except ZeroDivisionError:
            print("Rivi",str(rivimaara)+": Nollalla ei voi jakaa.")
        except ValueError:
            print("Rivi",str(rivimaara)+": Rivillä ei ollut numerodataa.")
        except IndexError:
            print("Rivi",str(rivimaara)+": Rivillä ei ole riittävästi lukuja.")
    tiedosto.close
        
    
paaohjelma()
