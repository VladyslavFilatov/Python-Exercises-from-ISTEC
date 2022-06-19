print("Introduza 10 numeros")
newlist = []
pares = []
for num in range(10):
    i = int(input())
    newlist.append(i)
cont = 0
sum = 0
for num in newlist:
    if num % 2 == 0:
        cont += 1
        sum += num
        pares.append(num)
print(f"Esta {cont} numeros pares em vetor")
print(f"Soma dos numeros pares é {sum}")
print(f"São numers pares {pares}")
input()
