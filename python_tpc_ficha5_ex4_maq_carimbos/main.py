print("Introduza uma operação: Ligar, Desligar, Carimbar")
operacao = str(input())
match operacao:
    case "Ligar": print("Ligar")
    case "Desligar": print("Desligar")
    case "Carimbar": print("Carimbar")
    case unknown_command:
        print("Error")
input()