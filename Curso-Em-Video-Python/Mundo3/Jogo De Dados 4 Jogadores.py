from random import randint 
import time
from operator import itemgetter
print("\033[35m4 Jogadores Jogarão Um Dado De 6 Lados e Você Terá que Acertar Quem Irá Ganhar!!!")
rank = []
erros = 0
acertos = 0
jogadas = "1","2","3","4"
while True:
    print("\033[0;36m=-"*20)
    
    escolha = input("\033[35mEm Qual Jogador Você Quer Apostar?(1-4)\033[33m ")
    if escolha == "0":
        print("\033[1;31mPrograma Finalizado!!!\033[0;37m")
        break
    while escolha not in jogadas:
        print("\033[31mINVÁLIDO!!!")
        escolha = input("\033[35mEm Qual Jogador Você Quer Apostar?(1-4) ou 0 Para Finalizar!!\033[33m ")

    jogo = {"jogador 1": randint(1, 6), "jogador 2": randint(1, 6), "jogador 3": randint(1, 6), "jogador 4": randint(1, 6)
}


    rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)

    
    for p, i in enumerate(rank):
        print(f"{p+1}° Lugar - {i[0]} com {i[1]} Pontos!!")
        time.sleep(1)

    jogador_e = f"jogador {escolha}"

    time.sleep(0.1)
    if jogador_e == rank[0][0]:
        print(f"\033[02;32m{'Você Acertou!!':>20}\033[0;37m")
        acertos += 1

    else:
        print(f"\033[3;31m{'Você Errou!!!':>20}\033[0;37m")
        erros += 1 

time.sleep(0.7)
print("\033[0;36m=-"*20)
time.sleep(0.5)
print(f"\033[0;35mVocê Chegou Ao Final\nVocê Acertou \033[1;32m{acertos}\033[0;35m Vez(es)\nVocê Errou \033[1;31m{erros}\033[0;35m Vez(es)!!")