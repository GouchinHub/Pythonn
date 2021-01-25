# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 18.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

import datetime
import sys
import numpy

## Luokka päivamäärän, tuntien, ja paisteajan seuraamista varten.

class HAVAINTOASEMA():   
    pvm = ""
    paiste = 0
    pvmtunnit = ""

## Valikko joka kertoo käyttäjälle ohjelman toiminnot, sekä kysyy ja testaa valinnan toimivuuden.

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Anna havaintoasema ja vuosi")
    print("2) Lue säätilatiedosto")
    print("3) Analysoi päivittäiset säätilatiedot")
    print("4) Tallenna päivittäiset säätilatiedot")
    print("5) Lue Ilmatieteen laitoksen tiedosto")
    print("6) Analysoi kuukausittaiset säätilatiedot")
    print("7) Tallenna kuukausittaiset säätilatiedot")
    print("8) Analysoi tuntikohtaiset säätilatiedot")
    print("9) Tallenna tuntikohtaiset säätilatiedot")
    print("0) Lopeta")
    try:
        valinta = int(input("Valintasi: "))
        if valinta >= 0 and valinta <= 9:
            return valinta
        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
            return None
    except ValueError:
        print("Anna valinta kokonaislukuna.")
        return None

## 1 Aliohjelma havaintoaseman nimen ja vuoden määrittämiseksi. palauttaa nimen ja vuoden listana paaohjelmaan.
    
def havainto_vuosi():
    nimijavuosi = []
    nimi = input("Anna havaintoaseman nimi: ")
    try:
        vuosi = int(input("Anna analysoitava vuosi: "))
    except ValueError:
        print("Anna vuosiluku kokonaislukuna.")
        return nimijavuosi
    nimijavuosi.append(nimi)
    nimijavuosi.append(vuosi)
    return nimijavuosi

## 2 Aliohjelma joka lukee ja listaa havaintoaseman tiedot.

def lue_tiedosto(nimijavuosi):
    try:
        nimijavuosi[0]       #Testaa onko parametrina saatu lista tyhjä, toistuu muissa aliohjelmissa.
    except IndexError:
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        return nimijavuosi
    lista = []      #Luo listan jonne luetut tiedot tallennetaan.
    nimi = ("{0:s}{1:d}.txt").format(nimijavuosi[0],nimijavuosi[1])
    try:
        tiedosto = open(nimi, 'r' ,encoding="utf-8")
    except OSError:
        print("Tiedoston '"+nimi+"' avaaminen epäonnistui.")
        sys.exit(0)
    try:
        rivinpoisto = tiedosto.readline()
    except OSError:
        print("Tiedoston '"+nimi+"' lukeminen epäonnistui.")
        sys.exit()
    rivimaara = 1
    while True:
        try:
            rivi = tiedosto.readline()
        except OSError:
            print("Tiedoston '"+nimi+"' lukeminen epäonnistui.")
            sys.exit()
        rivimaara += 1
        if len(rivi) == 0:
            break
        data = HAVAINTOASEMA()
        alkio = rivi.split(';')
        data.pvm = datetime.datetime.strptime(alkio[0],"%Y-%m-%d") #pelkkä päivämäärä
        pvmjatunnit = '{0} {1}'.format(alkio[0],alkio[1]) #Muuttaa alkioina saadun tiedon paivamaara ja tunnit muotoon.
        data.pvmtunnit = datetime.datetime.strptime(pvmjatunnit,"%Y-%m-%d %H:%M") #päivämäärä ja tunnit
        data.paiste = int(alkio[2])
        lista.append(data)
    print("Tiedosto '{0:s}' luettu. Tiedostossa oli {1:d} riviä.".format(nimi,rivimaara))
    tiedosto.close()
    return lista

## 3 Aliohjelma joka analysoi saadut tiedot ja laskee päivittäisen paisteajan kumulatiivisen summan.

def paivittainen_analysointi(lista):
    try:
        lista[0]
    except IndexError:
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return lista
    datalista = []  #Luodaan lista jonne analysoidut tiedot tallennetaan.
    paiva = lista[0].pvm
    summa = 0
    for alkio in lista:
        if (alkio.pvm == paiva):
            summa += int(alkio.paiste)
        else:
            data = HAVAINTOASEMA()
            data.pvm = paiva
            data.paiste = summa
            datalista.append(data)
            paiva = alkio.pvm
            summa += int(alkio.paiste)
    data = HAVAINTOASEMA()
    data.pvm = paiva
    data.paiste = summa
    datalista.append(data)
    print("Data analysoitu ajalta {0:s} - {1:s}.".format(datalista[0].pvm.strftime("%d.%m.%Y"),datalista[-1].pvm.strftime("%d.%m.%Y")))
    return datalista

## 4 Aliohjelma joka kirjoittaa analysoidun tiedot oikeassa muodossa uuteen tiedostoon.

def paivittainen_tallennus(datalista, nimijavuosi):
    try:
        datalista[0]
    except IndexError:
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        return datalista
    tnimi = input("Anna tulostiedoston nimi: ")
    try:
        tiedosto = open(tnimi, 'w')
    except OSError:
        print("Tiedoston '"+tnimi+"' avaaminen epäonnistui.")
        sys.exit(0)
    try:
        tiedosto.write("Pvm")
        for i in range(len(datalista)):
            tiedosto.write(";"+str(datalista[i].pvm.strftime("%d.%m.%Y")))
        tiedosto.write("\n"+str(nimijavuosi[0]))
        for i in range(len(datalista)):
            tiedosto.write(";"+str(int(datalista[i].paiste/60)))
        tiedosto.write("\n")
    except OSError:
        print("Tiedoston '"+tnimi+"' kirjoitus epäonnistui.")
        sys.exit(0)
    tiedosto.close()
    print("Paisteaika tallennettu tiedostoon '"+str(tnimi)+"'.")
    return None

## 5 Aliohjelma joka lukee ja listaa havaintoaseman tiedot.

def ilmatieteen_laitos(nimijavuosi):
    try:
        nimijavuosi[0]
    except IndexError:
        print("Valitse havaintoasema ja vuosi ennen tiedostonlukua.")
        return nimijavuosi
    lista = []  #Luo listan jonne luetut tiedot tallennetaan.
    nimi = ("{0:s}{1:d}_fmi.txt").format(nimijavuosi[0],nimijavuosi[1])
    try:
        tiedosto = open(nimi, 'r' ,encoding="utf-8")
    except OSError:
        print("Tiedoston '"+nimi+"' avaaminen epäonnistui.")
        sys.exit(0)
    try:
        rivinpoisto = tiedosto.readline()
    except OSError:
        print("Tiedoston '"+nimi+"' lukeminen epäonnistui.")
    rivimaara = 1
    while True:
        try:
            rivi = tiedosto.readline()
        except OSError:
            print("Tiedoston '"+nimi+"' lukeminen epäonnistui.")
        rivimaara += 1
        if len(rivi) == 0:
            break
        data = HAVAINTOASEMA()
        alkio = rivi.split(',')
        paivamaara = '{0}-{1}-{2}'.format(alkio[0],alkio[1],alkio[2])#Muuttaa alkioina saadun tiedon paivamaara muotoon.
        pvmjatunnit = '{0}-{1}-{2} {3}'.format(alkio[0],alkio[1],alkio[2],alkio[3])
        data.pvm = datetime.datetime.strptime(paivamaara,"%Y-%m-%d") #pelkkä päivämäärä
        data.pvmtunnit = datetime.datetime.strptime(pvmjatunnit,"%Y-%m-%d %H:%M") #päivämäärä ja tunnit
        try:
            data.paiste = int(alkio[5]) #testataan puuttuuko tiedoista paisteaika.
        except ValueError:
            data.paiste = 0 #jos puuttuu, listataan paisteajaksi 0.
        data.tunnit = alkio[3]
        lista.append(data)
    print("Tiedosto '{0:s}' luettu. Tiedostossa oli {1:d} riviä.".format(nimi,rivimaara))
    tiedosto.close()
    if lista[-1].pvmtunnit.strftime("%Y") > lista[-2].pvmtunnit.strftime("%Y"): #tarkistetaan viimeisen rivin vuosi
        del lista[-1] #poistetaan listasta jos vuosi vaihtunut.
    return lista

## 6 Aliohjelma joka analysoi saadut tiedot ja laskee kuukausittaisen paisteajan summan.

def kuukausittainen_analysointi(lista):
    try:
        lista[0]
    except IndexError:
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return lista
    datalista = [] #Luodaan lista jonne analysoidut tiedot tallennetaan.
    kuukausi = lista[0].pvmtunnit.strftime("%m")
    summa = 0
    for alkio in lista:
        if (alkio.pvmtunnit.strftime("%m") == kuukausi):
            summa += int(alkio.paiste)
        else:
            data = HAVAINTOASEMA()
            data.pvmtunnit = kuukausi
            data.paiste = summa
            datalista.append(data)
            kuukausi = alkio.pvmtunnit.strftime("%m")
            summa = int(alkio.paiste)
    data = HAVAINTOASEMA()
    data.pvmtunnit = kuukausi
    data.paiste = summa
    datalista.append(data)
    print("Data analysoitu ajalta {0:s} - {1:s}.".format(lista[0].pvmtunnit.strftime("%d.%m.%Y"),lista[-1].pvmtunnit.strftime("%d.%m.%Y")))
    return datalista

## 7 Aliohjela joka kirjoittaa analysoidut tiedot uuteen tiedostoon.

def kuukausittainen_tallennus(datalista,nimijavuosi, lippu):
    try:
        datalista[0]
    except IndexError:
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        return datalista
    if lippu == True:       #Kun aliohjelma suoritetaan ensimmäisen kerran, Kirjoitetaan uusi tiedosto.   
        tnimi = input("Anna kuukausitiedoston nimi: ")
        try:
            tiedosto = open(tnimi, 'w')
        except OSError:
            print("Tiedoston '"+tnimi+"' avaaminen epäonnistui.")
            sys.exit(0)
        try:
            tiedosto.write("Kk")        #Tiedostoon kirjoitetaan otsikkorivi josta näkyy kuukaudet.
            for i in range(len(datalista)):
                tiedosto.write(";"+str(datalista[i].pvmtunnit))
            tiedosto.write("\n{0:s} {1:d}".format(nimijavuosi[0],nimijavuosi[1]))
            for i in range(len(datalista)):     #Kirjataan kuukausittaiset paisteajat.
                tiedosto.write(";"+str(int(datalista[i].paiste/60)))
            tiedosto.write("\n")
        except OSError:
            print("Tiedoston '"+tnimi+"' kirjoitus epäonnistui.")
            sys.exit(0)
        tiedosto.close()
        print("Paisteaika tallennettu tiedostoon '"+str(tnimi)+"'.")
        return False   #Palautetaan lippu falsena aliohjelman käytön merkiksi.
    else:       #Kun aliohjelmaa on jo käytetty aikaisemmin on lippu == false.
        tnimi = input("Anna kuukausitiedoston nimi: ")
        try:
            tiedosto = open(tnimi, 'a')     #avataan tiedosto 'a' muodossa lisä kirjoittamista varten.
        except OSError:
            print("Tiedoston '"+tnimi+"' avaaminen epäonnistui.")
            sys.exit(0)
        try:
            tiedosto.write("{0:s} {1:d}".format(nimijavuosi[0],nimijavuosi[1]))
            for i in range(len(datalista)):     #Kirjataan kuukausittaiset paisteajat.
                tiedosto.write(";"+str(int(datalista[i].paiste/60)))
            tiedosto.write("\n")  
        except OSError:
            print("Tiedoston '"+tnimi+"' kirjoitus epäonnistui.")
            sys.exit(0)
        tiedosto.close()
        print("Paisteaika tallennettu tiedostoon '"+str(tnimi)+"'.")
        return False #Palautetaan lippu falsena aliohjelman käytön merkiksi.

## 8 Aliohjelma joka analysoi saadut tiedot ja laskee tuntikohtaisen kulutuksen joka kuukaudessa,
## ja luo tiedoista matriisin.

def tuntikohtainen_analysointi(lista):
    try:
        lista[0]
    except IndexError:
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return lista
    data = HAVAINTOASEMA()
    datamatriisi = numpy.zeros((24,12), int) #Luodaan matriisi jonne analysoidut tiedot tallennetaan.
    for alkio in lista:
        kk = alkio.pvmtunnit.month - 1
        hh = alkio.pvmtunnit.hour
        datamatriisi[hh][kk] += alkio.paiste
    print("Data analysoitu ajalta {0:s} - {1:s}.".format(lista[0].pvmtunnit.strftime("%d.%m.%Y"),lista[-1].pvmtunnit.strftime("%d.%m.%Y")))
    return datamatriisi

## 9 Aliohjelma joka luo tekstitiedoston ja kirjaa sinne analysoidut tiedot oikeassa muodossa.

def tuntikohtainen_kirjoitus(datamatriisi, nimijavuosi):
    try:
        datamatriisi[0][0]   #testaa onko matriisi tyhjä.
    except IndexError:
        print("Lista on tyhjä. Analysoi data ennen tallennusta.")
        return datamatriisi
    tnimi = ('{0:s}{1:d}tunnit.txt'.format(nimijavuosi[0],nimijavuosi[1]))  #Luo kirjoittaettavan tiedoston nimen.
    try:
        tiedosto = open(tnimi, 'w')  
    except OSError:
        print("Tiedoston '"+tnimi+"' avaaminen epäonnistui.")
        sys.exit(0)
    try:
        tiedosto.write("{0:s} {1:d} tuntipohjainen paisteaika:\n".format(nimijavuosi[0],nimijavuosi[1]))
        for hh in range(24):
            tiedosto.write(";"+str(hh))   #Kirjoittaa otsikkorivin jossa näkyy tunnit.
        tiedosto.write("\n")
        for hh in range(12):
            tiedosto.write(str(hh+1))
            for kk in range(24):
                tiedosto.write(";"+str(int(datamatriisi[kk][hh]/60)))
            tiedosto.write("\n")
        tiedosto.write("Yht.")
        for hh in range(24):
            tiedosto.write(";"+str(int(sum(datamatriisi[hh])/60)))
        tiedosto.write("\n")
    except OSError:
        print("Tiedoston '"+tnimi+"' kirjoitus epäonnistui.")
        sys.exit(0)
    tiedosto.close()
    print("Paisteaika tallennettu tiedostoon '"+str(tnimi)+"'.")
    return None

##########################################################################################
#eof
