def erro_int(txt):
    while True:
                try:
                    return int(input(txt))
                except ValueError:
                       print("\033[31mErro: Por Favor, Digite Um Número Válido.")
                except KeyboardInterrupt:
                       print("\033[31mO Usuário Preferiu Não Digitar Esse Número.")
                       return 3


def linha(tam=25):
    return "\033[34m=-"*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(25))
    print(linha())


def menu(lista):
    cabeçalho(f"\033[1;32m{"Menu Principal":>31}\033[0;32m")
    c = 1
    for i in lista:
        print(f"\033[32m{c} - {i}")
        c+= 1
    print(linha())
    opc = erro_int("\033[35mSua Opção:\033[33m ")
    return opc