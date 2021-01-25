#05-01 Aatu

x = int(input("Anna aloitusarvo: "))
y = int(input("Anna lopetusarvo: "))

print("Toteutus for-lauseella: ")
for p in range(x, y+1):
    print((p), end=" ")
print("")
print("")
print("Toteutus while-lauseella: ")

arvo = x
while (arvo < y+1):
    print((arvo), end=" ")
    arvo = arvo +1
    
