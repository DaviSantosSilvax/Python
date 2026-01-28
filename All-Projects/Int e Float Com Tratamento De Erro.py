print("\033[35mIrei Fazer Com Que Você Só Consiga Digitar Números Inteiros e Reais Utilizando Tratamento De Erro!")

def erro_int(txt):
    while True:
                try:
                    return int(input(txt))
                except ValueError:
                       print("\033[31mErro: Por Favor, Digite Um Número Inteiro Válido.")
                except KeyboardInterrupt:
                       print("\033[31mO Usuário Preferiu Não Digitar Esse Número.")
                       return 0
 


        
def erro_float(txt):
    while True:
                try:
                    return float(input(txt))
                except ValueError:
                       print("\033[31mErro: Por Favor, Digite Um Número Inteiro Válido.")
                except KeyboardInterrupt:
                       print("\033[31mO Usuário Preferiu Não Digitar Esse Número.")
                       return 0


i = erro_int("\033[35mDigite Um Inteiro:\033[33m ")
r = erro_float("\033[35mDigite Um Real:\033[33m ")

print(f"\033[35mO Valor Inteiro Foi Digitado Foi \033[32m{i}\033[35m e o Real Foi \033[32m{r}\033[37m")