print("\033[35mVou Ler 4 Valores e No Final Mostrar\n\033[36mQuantas Vezes Apareceu o Valor 9\nEm Que Posição Foi Digitado O Primeiro Valor 3\nQuais Foram Os Números Pares!!\033[37m")
print("\033[34m=-=-\033[35m"*20)
n1 = int(input("\033[35mDiga Um Valor:\033[33m "))
n2 = int(input("\033[35mDiga Outro Valor:\033[33m "))
n3 = int(input("\033[35mDiga Mais Um Valor:\033[33m "))
n4 = int(input("\033[35mDiga o Ultimo Valor:\033[33m "))
l = (n1, n2, n3, n4)
pares = ()
for n in l:
    if n % 2 == 0:
        pares += (n,)
print("\033[34m=-=-\033[35m"*20)
print(f"O Número 9 Apareceu {l.count(9)}")
print("\033[34m=-=-\033[35m"*20)
if 3 in l:
    print(f"O Primeiro 3 Apareceu Na Posição{l.index(3)}")
else:
    print(f"Não Houve Número 3")
print("\033[34m=-=-\033[35m"*20)
print(f"Os Números Pares São {pares}")

