#L03-05 Aatu

x = float(input("Anna pituus (senteissä): "))
y = float(input("Anna paino (kilogrammoissa): "))
z = float(round(y / ((x/100)**2), 1))

if(z < 15):
    print("Painoindeksi on",z ,"(Sairaalloinen alipaino)")
if(15 <= z < 17):
    print("Painoindeksi on",z ,"(Merkittävä alipaino)")
if(17 <= z < 18.5):
    print("Painoindeksi on",z ,"(Normaalia alhaisempi paino)")
if(18.5 <= z < 25):
    print("Painoindeksi on",z ,"(Normaali paino)")
if(25 <= z < 30):
    print("Painoindeksi on",z ,"(Lievä ylipaino)")
if(30 <= z < 35):
    print("Painoindeksi on",z ,"(Merkittävä ylipaino)")
if(35 <= z < 40):
    print("Painoindeksi on",z ,"(Vaikea ylipaino)")
if(40 <= z):
    print("Painoindeksi on",z ,"(HEIKKI TYNI)")

index = float(input("Anna tavoiteindexi: "))

if(z < index):
    print("Painoa tulis nostaa",round(index*((x/100)**2)-y,1),"kilogrammaa")
if(z > index):
    print("Painoa tulis tiputtaa",round(-index*((x/100)**2)+y,1),"kilogrammaa")
    



 
