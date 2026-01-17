print("\033[35mIrei Deixar Você Criar Um Boletim e Deixar Você Ver As Notas Individuais Posteriormente!!! ")

def frot(msg):
      while True:
            try:
                  return float(input(msg))
            except ValueError:
                    print("\033[31mDigite Um Válor!!")
mediia = 0
b = []
f = True
while f:
    nome = input("\033[35mNome:\033[33m ").title()
    nota1 = frot("\033[35mNota 1:\033[33m ")
    nota2 = frot("\033[35mNota 2:\033[33m ")
    media = (nota1+nota2)/2
    aluno = [nome, [nota1], [nota2], media]
    b.append(aluno)


    c = input("\033[35mDeseja Finalizar? [ \033[31mN\033[35m ] Para Finalizar: \033[33m")
    if c == "n":
          f = False

print(f"\033[35m{"Nome:":<5}{"Média:":>13}")
for i in b:
    print(f"\033[36m{i[0]:<5}{i[3]:>11}")

f = True
while f:
      a = input("\033[35mDeseja Mostrar Nota De Qual Aluno? \033[31m(999 Interrompe)\033[35m:\033[33m ").title()
      
      for i in b:
         if a == "999":
            f = False   
            print("\033[31mPrograma Finalizado!!!\033[37m")
         elif a not in i[0]:
                print("\033[31mAluno Não Encontrado!!")
         elif a == i[0]:
                            print(f"\033[36mAs Notas Do Aluno {i[0]} São: \033[32m\nNota1 ({i[1][0]}) e Nota2 ({i[2][0]})\033[35m")





