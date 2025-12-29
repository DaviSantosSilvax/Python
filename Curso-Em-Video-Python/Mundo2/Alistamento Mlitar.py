from datetime import date

data = date.today()
atual = data.year

print(atual)
nome = str(input("Olá, Qual Seu Nome? "))
ano = int(input("Tudo bem {}, Em que ano você nasceu??? " .format(nome)))
tempo = atual - ano
atraso = tempo - 18
falta = 18 - tempo

if 120 < tempo or tempo < 0:
    print("Digite Uma Idade Válida")
elif tempo > 18:
    print("Você Já passou do seu alistamento militar!!! ")
    print(f"Inclusive já se passaram {atraso} ano(s), {nome}")

elif tempo == 18:
    print("Está na hora de se apresentar ao exercito Brasileiro!!! ")


else:
    print("Você ainda vai se alistar ao serviço militar!!!")
    print(f"Faltam ainda {falta} ano(s) para se apresentar!! ")