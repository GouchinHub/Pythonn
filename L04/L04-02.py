#04-02 Aatu

n = 0
t = int(n)
sum = 0
while (n >= 0):
    n = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))
    if  (n == -1):
        break
    if (0 < n < 6):
        sum += n
        t += 1
    else:
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
KA = sum / t
karvo = round(KA,2)
print("Arvosanojen keskiarvo on", str(karvo) +".")
