print("Introduza factorial")
n = int(input())
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)
input()