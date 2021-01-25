#L03-03 aatu

x = int(input("Anna ensimmäinen luku: "))
y = int(input("Anna toinen luku: "))

print("Laskin osaa seuraavat toiminnot:")
print("1) Summa")
print("2) Erotus")
print("3) Tulo")
print("4) Osamäärä")
print("5) Potenssi")
print("Antamasi luvut ovat",x,"ja",y )
z = int(input("Valitse toiminto (1-5): "))
if(z == 1):
    print("Summa",x,"+",y,"=",x + y)
elif(z == 2):
    print("Erotus",x,"-",y,"=",x - y)
elif(z == 3):
    print("Tulo",x,"*",y,"=",x * y)
elif(z == 4):
    if(y == 0):
        print("Nollalla ei voi jakaa.")
    else:
        print("Osamäärä",x,"/",y,"=",round(x / y,2))
elif(z == 5):
    print("Potenssi"x,"^",y,"=",x ** y)
else:
    print("Toimintoa ei tunnistettu.")
print("Kiitos ohjelman käytöstä.")
