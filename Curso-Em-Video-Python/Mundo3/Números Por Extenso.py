print("\033[32mMe Fale Um Número \033[3;2mDe 0 Até 20\033[0;35m e Direi Como Se Escreve Ele Por \033[3;32mExtenso\033[0;35m!!!")
ex = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte"
)
while True:
    print("\033[3;36m===\033[0;35m"*20)
    while True:
        try:
            n = int(input("\033[35mDiga Um Número Inteiro?(Entre 0 e 20):\033[34m "))
            if 0 <= n <= 20:
                break
        except ValueError:
            print("\033[35merro, digite algo válido")
    print(f"\033[35mVocê Digitou \033[1;32m{n}\033[0;35m, Seu Número Por Extenso Fica \033[1;32m{ex[n]}\033[0;35m")
    f = input("\033[35mDeseja Continuar? \033[1;31m[N]\033[0;35m Para Não!!\033[34m ").lower
    if f == "n":
        break


