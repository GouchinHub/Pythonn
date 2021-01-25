#04-04 Aatu

x = int(input("Anna alueen alaraja: "))
y = int(input("Anna alueen yläraja: "))

for n in range(1):
    for i in range(x,y+1):
        if not i % 5 == 0:
            print(i ,"ei ole jaollinen viidellä, hylätään.")
            continue
        if i % 5 == 0 and not i % 7 == 0:
            print(i ,"ei ole jaollinen seitsemällä, hylätään.")
            continue
        if i % 7 == 0 and i % 5 == 0:
            print("Luku", i ,"on jaollinen 5:llä ja 7:llä.")
            print("Lopetetaan etsintä.")
            break
    else:
        print("Alueelta ei löytynyt sopivaa arvoa.")
