print("\033[35mIrei Te Mostrar o Fatorial De Um Número a Sua Escolha!!")

n = int(input("Me Diga Seu Número: \033[36m"))
f = 1
c = n
if n < 0:
    print("\033[35mFatorial Não Definido Para Valores Negativos!!")
elif n == 0:
    print("O Fatorial de 0 é 1!")
else:
    for i in range(1, n+1):
        f *= i
    print(f"Fatorial de {n} é {f}")