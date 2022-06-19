print("Introduza o lado A do triangulo")
L1 = float(input())
print("Intorduza o lado B do triangulo")
L2 = float(input())
print("Introduza o lado C do triangulo")
L3 = float(input())
reg = (L1 < L2 + L3) and (L2 < L1 + L3) and (L3 < L1 + L2)
isos = L1 == L2 and L1 != L3 and L2 != L3 or L1 != L2 and L1 == L3 and L2 != L3 or L1 != L2 and L1 != L3 and L2 == L3
esca = L1 != L2 and L2 != L3 and L1 != L3
igua = L1 == L2 and L2 == L3 and L1 == L3
if (reg):
    print("Triangulo")
    if (reg == isos):
        print(f"isoscelos:{L1,L2,L3}")
    elif (reg == esca):
        print(f"escaleno:{L1,L2,L3}")
    elif (reg == igua):
        print(f"tem todos lados iguais:{L1,L2,L3}")
else:
    print("Error")
input()