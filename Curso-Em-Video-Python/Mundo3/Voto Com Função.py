import time
from datetime import date
print("\033[35mIrei Dizer Se Seu Voto É Negado, Opcional Ou Obrigatório Usando De Parâmetro o Ano De Nascimento!!!")
data = date.today() 
hoje = data.year
def voto():
    print("\033[34m=-"*20)
    nasceu = int(input("\033[35mEm Que Ano Você Nasceu?\033[33m "))
    idade = hoje - nasceu
    if idade > 65:
        print(f"\033[35mCom \033[32m{idade}\033[35m Anos: Voto Opcional.")
    elif idade >= 18:
        print(f"\033[35mCom \033[32m{idade}\033[35m Anos: Voto Obrigatório.")
    elif idade < 18:
        print(f"\033[35mCom \033[32m{idade}\033[35m Anos: Não Vota.")

voto()
