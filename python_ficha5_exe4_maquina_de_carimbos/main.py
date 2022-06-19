print("Ola meo nome é Alise sou uma máquina de carimbos")
print("Liga me")
acao = str(input())
if acao == "ligar":
    print("Obrigada, espera um minuto")
else:
    print("Não consigo fazer essa operação. Liga me")
if acao == "ligar":
    print("Escolha operação: Carimbar ou Desligar")
acao = str(input())
while acao == "carimbar":
    print("Carimba feita com successo")
    print("Escolha operação: Carimbar ou Desligar")
    acao = str(input())
    if acao == "carimbar":
        continue
else: acao == "desligar"
print("Obrihada e bom dia")
input()