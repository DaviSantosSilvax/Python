print("\033[35mOrganizo 5 Valores Numéricos Sem Sort!!!\033[37")

def erro_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("\033[31mDigite Apenas Valores Válidos\033[35m")

n = [] 
for i in range(1,6):
    n.append(erro_int("\033[35mDigite O Valor:\033[33m "))
    print("\033[36m=-"*20)

f = True

while f:
    f = False
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            f = True
print(f"\033[35mSua Lista Em Ordem \033[32m{n}\033[37m")