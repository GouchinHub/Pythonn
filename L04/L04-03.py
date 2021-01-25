#L04-03

a = int(input("Anna a:n arvo: "))
b = int(input("Anna b:n arvo: "))

print("a:",a,"b:",b)
for i in range(1,100):
    a *= 2
    b += 100
    print("a:",a,"b:",b)
    if b > 10000 or a > b:
        break
print("Kiitos ohjelman käytöstä.")

