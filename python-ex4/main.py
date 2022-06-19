print("Introduza a nota do 1 exam")
n1 = float(input())
print("Introduza a nota do 2 exam")
n2 = float(input())
print("Introduza a nota do 3 exam")
n3 = float(input())
print("Introduza a nota do 4 exam")
n4 = float(input())
notas = n1 + n2 + n3 + n4
nfin = notas / 4
if nfin < 10:
    print(f"Aluno não aprovado:{nfin}")
else:
        print(f"Aluno aprovado:{nfin}")
input()