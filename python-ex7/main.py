print("Introduza a sua escolha - pedra, papel ou tesoura")
escolha1 = str(input())
print("Introduza a sua escolha pedra, papel ou tesoura")
escolha2 = str(input())
if ((escolha1=="pedra" and escolha2=="papel") or (escolha1=="papel" and escolha2=="tesoura") or (escolha1=="tesoura" and escolha2=="pedra")):
    print("Ganho jogador 2")
elif ((escolha1=="papel" and escolha2=="pedra") or (escolha1=="tesoura" and escolha2=="papel") or (escolha1=="pedra" and escolha2=="tesoura")):
    print("Ganho jogador 1")
else:
    print("Empate")
input()