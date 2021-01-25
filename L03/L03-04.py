#L03-04 Aatu

x = str(input("Anna sana 1: "))
y = str(input("Anna sana 2: "))

if(x < y):
    print("'"+x+"' on aakkosissa aiemmin kuin '"+y+"'.")
if(y < x):
    print("'"+y+"' on aakkosissa aiemmin kuin '"+x+"'.")
if(x == y):
    print("Sanat ovat samoja")
if('z')in(x):
    print("Kirjain 'z' löytyy sanasta 1.")
if('z')in(y):
    print("Kirjain 'z' löytyy sanasta 2.")
if('z')not in(y) and ('z')not in(x):
    print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.")

sana = str(input("Anna testattava sana: "))
if (sana == sana[::-1]):
    print("Antamasi sana '"+sana+"' on palindromi.")
else:
    print("Antamasi sana ei ole palindromi.")
    print("Se on väärinpäin '"+sana[::-1]+"' ja oikein päin '"+sana+"'.")

    
