print("\033[35mMe Diga a Razão, o Primeiro Termo e Quantos Termos Deseja da sua P.A!!!")

t = int(input("Me Diga o Primeiro Termo:\033[36m "))
r = int(input("\033[35mMe Diga a Razão:\033[36m "))

while t < 0:
    t = int(input("Digite um valor válido para o termo: "))

while r <= 0:
    r = int(input("Digite um valor válido para a razão: "))

while True:
    nt = int(input("\033[35mMe diga a quantidade de termos (0 para sair):\033[36m "))

    if nt == 0:
        print("\033[35mPrograma encerrado!\033[0m")
        break

    to = 0
    termo = t
    cont = nt

    while cont > 0:
        print(termo)
        to += termo
        termo += r
        cont -= 1

    print(f"\033[35mA soma dos \033[32m{nt} termos\033[35m é {to}")
