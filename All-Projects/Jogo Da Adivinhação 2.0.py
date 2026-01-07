import random
print("\033[0;35;40mHAHAHA Tente Adivinhar Meu Número Sécreto entre 0 e 10!!!")
secreto = random.randint(0, 10)
nt = 1
n = int(input("\033[0;35;40mQual Número vai tentar? \033[0;34;40m"))
while n != secreto:
     nt += 1
     n = int(input("\033[0;35;40mVocê errou!! Tente Novamente: \033[0;34;40m"))
print(f"Você Acertou!!! Meu Número Secreto Era \033[1;32;40m [{secreto}] \033[0;35;40m!! ")
print(f"Você tentou {nt} Vezes Para Acertar Meu Número!!! ")