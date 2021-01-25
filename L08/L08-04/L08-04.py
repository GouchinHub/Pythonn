# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Aatu Laitinen
# Opiskelijanumero: 0501379
# Päivämäärä: 4.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:

import datetime



VIIKKOJA = 54

lista = []
tuloslista = []

for i in range(VIIKKOJA):
    tuloslista.append(0)

tiedosto = open("2018Sahkonkulutus.txt", "r")
poistarivi = tiedosto.readline()
while True:
    rivi = tiedosto.readline()
    if len(rivi) == 0:
        break
    tiedot = rivi[:-1].split(';')
    aikatiedot = rivi[:-1].split(' ')
    pvm = datetime.datetime.strptime(tiedot[0], " %d.%m.%Y %H:%M")
    vknro = int(pvm.strftime("%W"))
    tuloslista[vknro] += int(tiedot[1])
    
for i in range(VIIKKOJA):
    print(i, end=';')
    print(tuloslista[i])
    
tiedosto.close()

print("Kiitos ohjelman käytöstä.")
