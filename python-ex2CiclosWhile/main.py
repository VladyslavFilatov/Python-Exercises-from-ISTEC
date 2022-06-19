newlist = []
i = str
while len(newlist) < 10 and i != "Stop":
    i = str(input("Escreve o seu nome: "))
    if i != "Stop":
        newlist.append(i)
    else:
        break
print(newlist)
input()