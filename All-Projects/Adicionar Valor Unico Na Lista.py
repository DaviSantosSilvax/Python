print("\033[35mIrei Adicionar Apenas Valores Unicos Na Lista e Não Permitir Valores Duplicados!!! E Mostrarei Os Valores Em Ordem Crescente Ao Final.")
def valores_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("\033[31mErro, Digite Valor Válido!!\033[35m")
n = []
f = True
while f:
    print("\033[36m=-="*20)
    valor = valores_int("\033[35mDigite Um Valor: \033[33m")

    if valor in n:
        print("\033[31mValor Duplicado!! Não Será Possivel Adicionar Valor!!")
    else:
        print("\033[32mValor Adicionado Com Sucesso!!!")
        n.append(valor)
        
    c = input("\033[35mDigite \033[31m[N] \033[35mPara Finalizar:\033[33m ".lower())
    if c == "n":
        f = False
        break

print(f"\033[35mVocê Digitou Os Valores \033[1;32m{sorted(n)}\033[0;37m")


























