import time
import random
print("Irei Sortear 5 Valores e Somar Os Números Pares Em Uma Lista De Números Utilizando Funções")
lista = list()
def sorteio():
    print("\033[35mSorteando 5 Valores Da Lista: ",end="")
    for n in range(5):       
        n = random.randint(1, 10)
        print(f"\033[32m{n}", end=" ", flush=True)
        lista.append(n)
        time.sleep(0.6)
    print() 
def soma():
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares += i
    print(f"\033[35mSomando Os Valores Pares de \033[32m{lista}\033[35m, temos \033[32m{pares}\033[35m.")
sorteio()
soma()
