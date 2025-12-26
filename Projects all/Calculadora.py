print("Calculadora basica de operações")
n1 = int(input("digite um numero "))
n2 = int(input("digite outro numero "))
operacao = input("digite a operação(+,-,*, /) ")

match operacao:
    case "+":
        res = n1 + n2
    case "-":
        res = n1 - n2
    case "/":
        res = n1 / n2
    case "*":
        res = n1 * n2
    case "_":
        res = "Invalido"
print(f"Seu resultado é {res}")
