import random
print("\033[35mVou Gerar 5 Números Aleatórios e Mostrar o Maior e Menor!!")
lista = ()
for i in range(0, 5):
    n = random.randint(0, 1000)
    lista += (n, )


print(f"Seu Números Foram \033[33m{lista}\033[35m")
print(f"O Maior Número é \033[33m{max(lista)}\033[35m e o Menor é \033[33m{min(lista)}\033[37m")
