#L02-05 Aatu Laitinen

print("Tämä ohjelma laskee antamiesi 3 lucun keskiarvon.")
x = int(input("Anna luku 0 ja 10 väliltä: "))
y = int(input("Anna toinen luku 0 ja 10 väliltä: "))
z = int(input("Anna toinen luku 0 ja 10 väliltä: "))

print("")

print("Antamiesi lukujen summa on", x+y+z, end='.\n')
karvo = float((x+y+z)/3)
print("Antamiesi lukujen keskiarvo on", karvo, end='.\n')
print("Keskiarvo on kokonaislukuna", int(karvo), end='.\n')
print("Keskiarvo pyöristettynä 3 desimaalin tarkkuuteen on", round(karvo, 3), end='.\n')



