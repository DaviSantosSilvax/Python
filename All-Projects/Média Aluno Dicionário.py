print("\033[35mVou Ler Nome e Média De Um Aluno e Mostrarei no Final Em Um Dicionário Juntamente Com a Situação Dele!!!")

def froat(msg):
      while True:
            try:
                  return float(input(msg))
            except ValueError:
                    print("\033[31mDigite Um Válor!!")

nome = str(input("\033[35mQual Nome Do Aluno?\033[33m "))
media = froat("\033[35mQual Média Deste Aluno?\033[33m ")
if media >= 7:
       boletim = {"nome":nome,"média":media,"Situação":"Aprovado!!"}
       print(f"\033[35mO Aluno:\033[36m{boletim['nome']}\033[35m, Está Com A Média \033[36m{boletim['média']}\033[35m, Ele Está Na Situação: \033[32m{boletim['Situação']}")
else:
       boletim = {"nome":nome,"média":media,"Situação":"Reprovado!!"}
       print(f"\033[35mO Aluno: \033[36m{boletim['nome']}\033[35m, Está Com A Média \033[36m{boletim['média']}\033[35m, Ele Está Na Situação: \033[31m{boletim['Situação']}")