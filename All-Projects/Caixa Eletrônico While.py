print("\033[35mSou Um Caixa Eletrônico e Tenho Notas De:\n\033[36mR$50, R$20, R$10 E R$1!!!")

while True:
    print("\033[3;36m===\033[0;35m" * 20)

    while True:
        try:
            n = int(input("\033[35mQuanto Você Deseja Sacar?(Número Inteiro):\033[34m "))
            if n >= 0:
                break
        except ValueError:
            print("\033[35mErro, digite um número válido")

    ced = 50
    total = 0

    while True:
        if n >= ced:
            n -= ced
            total += 1
        else:
            if total > 0:
                print(f"\033[32mTotal de {total} notas de R${ced}")
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            total = 0

            if n == 0:
                break

    break
