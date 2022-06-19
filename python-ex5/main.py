print("Introduza a nota do 1 test")
n1 = float(input())
print("Introduza a nota do 2 test")
n2 = float(input())
notas = n1 + n2
nfin = notas / 2
if nfin > 10:
    print(f"Aluno approvado:{nfin}")
else:
        print("Aluno não approvado, vai fazer exam")
        print("Introduza a nota do Exam")
        nexam = float(input())
        nfinal = nfin * 0.40 + nexam * 0.60
        if nfinal > 10:
            print(f"Aluno approvado:{nfinal}")
        else:
            print(f"Aluno não approvado:{nfinal}")
input()