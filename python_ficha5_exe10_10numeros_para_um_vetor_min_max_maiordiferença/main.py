print("Introduza 10 numeros")
newlist = []
dif = 0
for num in range(10):
    i = int(input())
    newlist.append(i)
newlist = sorted(newlist)
min = newlist[0]
max = newlist[9]
for n in range(min, max):
    dif +=1
dif2 = max - min
print(f"Numero minimo é {min}")
print(f"Numero maximo é {max}")
print(f"Diferença entre os numeros é {dif}")
print(dif2)
input()