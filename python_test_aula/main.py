print("Escreve o numero 1")
n1 = int(input())
print("Escreve o numero 2")
n2 = int(input())

print("Escreve o numero da elevaçãp")
n = int(input())

somma = n1 + n2

if somma % 2 == 0:
    print(f"somma dos numeros: {somma} é par")
    print(f"Soma + numero da elevação: {somma + n}")
else:
    print(f"somma dos numeros: {somma} é inpar")
    print(f"Soma + numero da elevação: {somma + n}")
input()


