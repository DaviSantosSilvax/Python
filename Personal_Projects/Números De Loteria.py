import random
print("\033[35mIrei Sortear Números Para Você Jogar Na MegaSena De Para Quantas Vezes Você Quise")
def erro_int(txt):
    while True:
                try:
                    return int(input(txt))
                except ValueError:
                       print("\033[31mErro: Por Favor, Digite Um Número Inteiro Válido.")
                except KeyboardInterrupt:
                       print("\033[31mO Usuário Não Digitou Valor.")
                       return 0
                

n = erro_int("\033[35mQuantas Vezes Você Vai Jogar?\033[33m ")

lista = list()

for i in range(n):
    jogo = random.sample(range(1,61), 6)
    lista.append(jogo)

print(f"\033[35mSeus \033[1;32m{n}\033[0;35m Jogo(s) Deram Estes Valores No Sorteio:")
if n == 0:
      print("\033[31mNenhum Jogo Foi Gerado.\033[37m")
else:
    for i,jogos in enumerate(lista):
        print(f"\033[35mJogo {i+1} \033[33m-\033[32m {jogos}\033[37m")
