print("\033[1;35mIrei Ler Nome E Peso De Várias Pessoas Em Uma Lista e No Final Dizer:")
print("\033[0;35mQuantas Pessoas foram Cadastradas")
print("Uma Listagem Com As Pessoas Mais Pesadas.")
print("Uma Listagem Com As Pessoas Mais Leves")
print("\033[36m-_" * 20)

def inte(txt):
    while True:
        try:
            return int(input(txt))
        except ValueError:
            print("\033[31mInsira Um Valor Válido!!!")

pessoas = []
peso_maior = 0
peso_menor = 0
mais_pesadas = []
mais_leves = []

while True:
    nome = input("\033[35mDigite Seu Nome:\033[33m ").title()
    peso = inte(f"\033[35mDigite o Peso de {nome}:\033[33m ")

    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        peso_maior = peso_menor = peso
        mais_pesadas = [nome]
        mais_leves = [nome]
    else:
        if peso > peso_maior:
            peso_maior = peso
            mais_pesadas = [nome]
        elif peso == peso_maior:
            mais_pesadas.append(nome)

        if peso < peso_menor:
            peso_menor = peso
            mais_leves = [nome]
        elif peso == peso_menor:
            mais_leves.append(nome)

    c = input("\033[35mDeseja Finalizar? Digite [\033[32mN\033[35m]:\033[33m ").lower()
    print("\033[36m-_" * 20)
    if c == "n":
        break

print(f"\033[35mForam Cadastradas \033[1;32m{len(pessoas)}\033[0;35m Pessoas")
print(f"\033[35mPessoas mais pesadas ({peso_maior}kg): \033[32m{mais_pesadas}")
print(f"\033[35mPessoas mais leves ({peso_menor}kg): \033[32m{mais_leves}")
