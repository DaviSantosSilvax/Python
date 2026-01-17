print("\033[35mIrei Ler Seus Números Em Ordem Para Colocalos Em Uma Matriz 3x3")
def inte(msg):
      while True:
            try:
                  return int(input(msg))
            except ValueError:
                    print("\033[31mDigite Um Válor!!")
lista = [[], [], []]

for l in range(3):
       for c in range(3):
        n = inte(f"\033[35mDigite Um Valor Para [{l}, {c}]: ")
        lista[l].append(n)

print("\nMatriz 3x3:")
for i in lista:
    print(i)