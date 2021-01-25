# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 29.10.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: Tuomas Kujala, kuinka lukea viikot matriisissa

import datetime
import numpy

class TIEDOT():
    kulutus = 0
    pvm = ""

KUUKAUSIA = 12
TUNTEJA = 24

lista = []
matriisi = numpy.zeros((KUUKAUSIA,TUNTEJA), int)
 
tiedosto = open("2018Sahkonkulutus.txt")
poistarivi = tiedosto.readline()
while True:
    rivi = tiedosto.readline()
    if len(rivi) == 0:
        break
    tiedot = rivi[:-1].split(';')
    aikatiedot = rivi[:-1].split(' ')
    data = TIEDOT()
    data.pvm = datetime.datetime.strptime(aikatiedot[1], "%d.%m.%Y")
    data.kulutus = int(tiedot[1])
    lista.append(data)

    
tiedosto.close()

for alkio in lista:
    vk = int(alkio.pvm.strftime("%W"))
    matriisi[vk] += alkio.kulutus


for vk in range(VIIKKOJA):
    print(str(vk), end=';')
    print(str(matriisi[vk]))

print("Kiitos ohjelman käytöstä.")
