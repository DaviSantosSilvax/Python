print("\033[35mDigite 7 Números e Irei Separar Eles Em Uma Lista e Deixar Tudo Em Ordem Crescente")
lista = [[], []]
def inte(msg):
      while True:
            try:
                  return int(input(msg))
            except ValueError:
                    print("\033[31mDigite Um Válor!!")

for i in range(1,8):
    n = inte(f"\033[35mDigite o Seu {i}° Número:\033[33m ")

    while n in lista[0] or n in lista[1]:
            n = inte("\033[31mDigite Um Número Novo!!\033[33m ")

    if n % 2 == 0:
          lista[0].append(n)
    else:
          lista[1].append(n)
          

    i+= 1
    

print(f"\033[35mSua Lista De Números Pares é {sorted(lista[0])}")
print(f"\033[35mSua Lista De Números Impares é {sorted(lista[1])}")