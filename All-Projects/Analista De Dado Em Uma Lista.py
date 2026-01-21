print("\033[3;35mIrei Ler Seus Números Inseridos Em Uma Lista E Dizer, \033[3;32mQuantos Números Foram Digitados, A Lista Decrescente e Se Existe o Valor 5 Na Lista\033[3;35m!!")

def erro_int(txt):
    while True:
        try:
            return int(input(txt))
        except ValueError:
            print("\033[3;31mErro!! Digite Números Válidos")
            
f = True
n = []
while f:
    n.append(erro_int("\033[0;35mDigite Um Número:\033[33m "))
    c = input("\033[35mDeseja Finalizar? Para Finalizar Digite [ \033[3;31mN \033[0;35m]\033[33m ").lower()
    if c == "n":
        f = False
        break

print("\033[35m=-"*20)
print(f"Existem {len(n)} Números Na Sua Lista")
print("\033[35m=-"*20)
print(f"\033[35mSua Lista Em Ordem Decrescente\033[32m {sorted(n, reverse=True)}")
print("\033[35m=-"*20)
if 5 in n:
    print("\033[32mO Valor 5 Existe Na Lista!!")
else:
    print("\033[31mO Valor 5 Não Existe Na Lista!!")