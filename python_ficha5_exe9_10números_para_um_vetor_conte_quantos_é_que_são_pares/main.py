newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
cont = 0
sum = 0
for item in newlist:
    if item % 2 == 0:
        cont += 1
        sum += item
        pares.append(item)
print(f"Esta {cont} numeros pares em vetor")
print(f"Soma dos numeros pares é {sum}")
print(f"São numers pares {pares}")
input()