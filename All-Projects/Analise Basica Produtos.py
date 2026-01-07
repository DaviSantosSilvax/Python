print("\033[3;35mIrei Ler Nome e Preço De Seus Produtos.\n\033[0;34mIrei Mostrar:\nQual Total Gasto Na Compra.\nQuantos Produtos Custam Mais de R$1.000.\nQual é o Nome Do Produto Mais Barato")

f = True
t = 0
pm = 0
pb = float("inf")
pbb = "n"

while f:
    print("\033[34m==="*20)
    nome = input("\033[35mQual Nome Deste Produto?\033[33m ")

    while True:
        try:
            preço = float(input("\033[35mQual Valor Deste Produto?\033[33m "))
            while preço < 0:
                preço = float(input("\033[35mDigite Um Valor Válido: "))
            break
        except ValueError:
            print("\033[35merro, digite algo válido")
            
    t += preço
    if preço > 1000:
        pm += 1
    if preço < pb:
        pb = preço
        pbb = nome

    c = input("\033[35mDigite \033[1;32m[C]\033[0;35m Para Contincuar e \033[1;31m[S]\033[0;35m Para Sair: ").lower()
    if c == "c":
        continue
    elif c == "s":
        f = False
        break
    else:
        c = input("\033[35mDigite \033[1;32m[C]\033[0;35m Para Contincuar e \033[1;31m[S]\033[0;35m Para Sair: ").lower()
print("\033[34m==="*20)
print(f"\033[35mO Total Gasto Na Sua Compra Foi De R$\033[1;32m{t}\033[35m!!!")
print(f"\033[35mSua Compra Foi De \033[1;32m{pm}\033[0;35m Produtos Que Custam Mais de R$1.000!!!")
print(f"\033[35mSeu Produto Mais Barato Foi O \033[1;32m{pbb}\033[0;35m com preço de \033[1;32m{pb:.2f}\033[0;35m!!!\033[37m")