print("Digo se um Ano é bissexto ou não!!")

while True:
    ano = int(input("Diga um ano, direi se ele é Bissexto!!!: "))

    if ano  == 0:
        print("Programa encerrado!!!")
        break

    elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é Bissexto!!!!")

    else:
          print(f"O ano {ano} não é Bissexto!!!!")
    