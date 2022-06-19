print("Introduza um numero")
num = int(input())
i = num - 1
primo = True
while i > 1 and primo == True:
    if num % i == 0:
        primo = False
    i -= 1
if primo == True:
    print(f"numero primo:{num}")
else:
    print(f"numero não primo:{num}")
input()