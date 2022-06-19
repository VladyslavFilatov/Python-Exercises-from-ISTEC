print("Introduza os numeros")
a, b, c = int(input()), int(input()), int(input())
if a > b and a > c:
    print(f"Numero maximo é {a}")
elif b > a and b > c:
    print(f"Numero maximo é {b}")
else:
    print(f"Numero maximo é {c}")
input()

