print("Escolha a sua moeda - Euro ou Dolares")
m = str(input())
print("Introduza o numero")
n = float(input())
dolar = n * 1.19
euro = n / 1.19
if (m == "Euro"):
    print(f"Obrigado, valor em dolares {dolar}")
else:
    print(f"Obrigado, valor em euro {euro}")
input()