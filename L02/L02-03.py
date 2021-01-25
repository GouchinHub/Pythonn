#L02-04

x = int(input("Anna positiivinen kokonaisluku: "))

print("Luku", x,"kerrottuna itsellään on", x*x)

r = int(input("Anna ympyrän säteen pituus kokonaislukuna: "))

pii = float(3.14)

print("Ympyrän säde on", r, end=',')
print(" kehä on", 2*r*pii ,"ja pinta-ala on", pii*r**2, end='.\n')

t = int(input("Anna suorakulmion yhden sivun pituus kokonaislukuna: "))
t2 = int(input("Anna suorakulmion toisen sivun pituus kokonaislukuna: "))

print("Suorakulmion sivut ovat", t,"ja",t2, end=';')
print(" kehä on",2*t+2*t2, end=';')
print(" ja pinta-ala on", t*t2, end='.')
