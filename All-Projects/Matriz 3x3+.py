print("\033[35mIrei Ler Seus Números Em Ordem Para Colocalos Em Uma Matriz 3x3")
def inte(msg):
      while True:
            try:
                  return int(input(msg))
            except ValueError:
                    print("\033[31mDigite Um Válor!!")
lista = [[], [], []]
pares = 0

for l in range(3):
       for c in range(3):
        n = inte(f"\033[35mDigite Um Valor Para [{l}, {c}]: ")
        if n % 2 == 0:
             pares += n
        lista[l].append(n)

soma = lista[0][2] + lista[1][2] + lista[2][2]
nl = sorted(lista[1], reverse = True)

print("\nMatriz 3x3:")
for i in lista:
    print(f"\033[1;33m{i}")

print(f"\033[0;35mA Soma Dos Valores pares é \033[32m{pares}\033[35m!!")
print(f"\033[0;35mA Soma Dos Valores Da Terceira Coluna É \033[32m{soma}\033[35m!!")
print(f"\033[0;35mO Maior Valor Da Segunda Linha É \033[32m{nl[0]}\033[35m!!")