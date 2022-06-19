def switch():
    operacao = str()
    while operacao != "Desligar":
        print("Introduza uma operação: Ligar, Desligar, Carimbar")
        operacao = str(input())
        if operacao == "Ligar":
            print("Ligar")
        elif operacao == "Desligar":
            print("Desligar")
        elif operacao == "Carimbar":
            print("Carimbar")
        else:
            print("Introduzia uma operação errada")
            continue
switch()
input()