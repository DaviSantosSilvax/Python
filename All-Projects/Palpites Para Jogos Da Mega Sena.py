import time
import random
print("\033[35mIrei Dar Palpites De Números Da Mega Sena Para Seus Jogos!!!")
def inte(msg):
      while True:
            try:
                  return int(input(msg))
            except ValueError:
                    print("\033[31mDigite Um Válor!!")

p = inte("\033[35mVocê Deseja Palpites Para Quantos Jogos?\033[33m ")
time.sleep(0.5)
print("\033[36m--"*20)
for i in range(0, p):
       n = random.sample(range(1,61), 6)
       print(f"\033[36m..::\033[35mJogo {i}\033[36m::.. \033[32m{n}")
       print("\033[36m--"*20)
       time.sleep(0.5)
       
print(f"\033[35mEsses São Seus {p} Palpites!!!")