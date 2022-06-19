print("Introduza os numeros")
num1 = int(input())
num2 = int(input())
total = 0
max = num1
min = num1
if num1 < num2:
    min = num1
    max = num2
else:
    min = num2
    max = num1
for i in range(num1+1, num2):
    total += i
min += 1
max -= 1
print(f"Soma entre dois numeros = {total}")
print(f"Numero minimo entre dois numeros = {min} e numero maximo = {max}")
input()

