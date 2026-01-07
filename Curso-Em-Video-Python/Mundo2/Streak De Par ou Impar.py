import random
print("\033[02;35mIrei Te Desafiar No Par Ou Impar, Só Irei Parar Quando Você Perder e Mostrar Quantas Vitórias Você Obteve\033[0;35m")
vitoria = 0
derrota = 0
while True:
    total = 0
    jogada = input("Digite Se Você Deseja Jogar Par ou Impar: \033[32m").lower()
    while jogada  not in("par", "impar"):
        jogada = input("Digite Uma Jogada Válida: ")
        continue
    if jogada == "impar":
        print("Você Escolheu Impar e a Maquina Par!!!")
    elif jogada == "par":
        print("Você Escolheu Par e a Maquina Impar!!!")

    n = int(input("\033[35mDigite Quanto Você Quer jogar(Apenas Números Positivos!!):\033[32m "))
    pc = random.randint(1, 10) 
    total = pc + n
    if total % 2 == 0 and jogada == "impar" or total % 2 != 0 and jogada == "par":
        print(f"Você é {jogada} e escolheu {n}, a maquina escolheu {pc}, o total deu {total}. Você PERDEU!!!")
        break
    else:
        print(f"Você é {jogada} e escolheu {n}, a maquina escolheu {pc}, o total deu {total}. Você GANHOU!!!")
        vitoria += 1

print("\033[1;31mVOCÊ PERDEU E O PROGRAMA FOI ENCERRADO!!!\033[0;32m") 
print(f"Você ganhou {vitoria}")