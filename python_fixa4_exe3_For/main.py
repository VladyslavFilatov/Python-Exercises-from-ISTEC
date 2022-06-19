print("Introduza factorial")
num = int(input())
factorial = 1
for num in range (num, 1, -1):
    factorial = factorial * num
print(factorial)