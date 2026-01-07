print("\033[35mSou Um Caixa Eletrônico e Tenho Notas De:\n\033[36mR$50, R$20, R$10 E R$1!!!")
f = True
c = 0
v = 0
d = 0
u = 0
r = 0
while f:
    print("\033[3;36m===\033[0;35m"*20)
    while True:
        try:
            n = int(input("\033[35mQuanto Você Deseja Sacar?(Número Inteiro):\033[34m "))
            while n < 0:
                n = int(input("\033[35mQuanto Você Deseja Sacar?(Número Inteiro):\033[34m "))
            break
        except ValueError:
            print("\033[35merro, digite algo válido")
            
    c = n // 50
    n = n % 50

    v = n // 20
    n = n % 20

    d = n // 10
    n = n % 10

    u = n // 1
    n = n % 1
    f = False
print(f"\033[35mVocê Vai receber \033[1;32m{c} \033[0;32mNotas De R$50\n\033[1;32m{v} \033[0;32mNotas De R$20\n\033[1;32m{d} \033[0;32mNotas De R$10\n\033[1;32m{u} \033[0;32mNotas de R$1")