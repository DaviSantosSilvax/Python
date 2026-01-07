print("\033[3;35mIrei Te Mostrar A Tabuada Dos Números Positivos Inteiros Solicitados!!\033[35m")

while True:
    n = int(input("\033[0;35mQuer ver a Tabuada de Qual Valor? Insira Número Negativo para encerrar:\033[32m "))
    print("===="*30)
    if n < 0:
        print("Encerrado!!!")
        break
    for i in range(0,11):
        print(f"{n} x {i} = {n*i}")
