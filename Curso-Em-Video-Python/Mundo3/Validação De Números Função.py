print("\033[35mIrei Fazer Uma Função Para Só aceitar Números")

def erro_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("\033[31mErro, Digite Um Número Inteiro!!!")


n = erro_int("\033[35mDigite Um Número:\033[33m ")

print(f"\033[35mVocê Acabou De Digitar O Número \033[32m{n}\033[35m.\033[37m")