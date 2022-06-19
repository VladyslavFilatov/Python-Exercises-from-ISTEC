import math
def resolvente(a, b, c):
    root = (b*b)-(4*a*c)
    if root < 0:
        return []
    total = []
    total.append((-b+math.sqrt(root))/(2*a))
    total.append((-b-math.sqrt(root))/(2*a))
    total.sort()
    return total


# Teste:
a = input(int)
b = -1
c = -30
print(resolvente(a, b, c))