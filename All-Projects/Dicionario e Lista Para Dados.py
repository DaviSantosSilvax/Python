print("\033[35mIrei Ler, Nome, Sexo e Idade De Pessoas, guardar os dados do dicionário em uma lista")
s = ["m", "f"]
p = 1
maiores = []
mediai = 0
lista = list()
cadastros = 0
maioresmedia = []
mulheres = []
def erro_int(txt):
    while True:
        try:
            return int(input(txt))
        except ValueError:
            print("\033[3;31mErro!! Digite Números Válidos")

while True:
    n = str(input("\033[35mQual Nome Desta Pessoa?\033[33m ")).title()
    while not n.replace(" ", "").isalpha():
        n = str(input("\033[35mQual Nome Desta Pessoa?\033[33m "))
    sexo = str(input("\033[35mQual Sexo Desta Pessoa?? \033[32m[M]\033[35m/\033[32m[F]\033[33m ")).lower()
    while sexo not in s:
        sexo = str(input("\033[35mQual Sexo Desta Pessoa?? \033[32m[M]\033[35m/\033[32m[F]\033[33m ")).lower()
    if sexo == "f":
        mulheres.append(n)
    idade = erro_int("\033[35mQual Idade Desta Pessoa\033[33m ")
            
    rg = {"Nome": n, "Sexo": sexo, "Idade": idade}
    if idade >= 18:
        maiores.append(rg.copy)
    lista.append(rg.copy())
    cadastros += 1
    mediai += idade
    c = input("\033[35mDigite [ \033[31mN\033[35m ] Para Finalizar:\033[33m ").lower()
    if c == "n":
        break
    print("\033[34m=-"*20)
mediai /= len(lista)

for i in lista:
    if i["Idade"] > mediai:
        maioresmedia.append(i.copy())

print("\033[35m=-"*20)
print(f"\033[35mO Grupo Tem {cadastros}.")
print(f"\033[35m Média De Idade é De {mediai}.")
print(f"As Mulheres Cadastradas foram {mulheres}.")
print(f"\033[35mA Lista De Pessoas Acima Da Média é:\n{maiores}")
print("\033[35m=-"*20)