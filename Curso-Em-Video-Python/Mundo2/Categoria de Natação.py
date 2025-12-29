from datetime import date

print("Você está na confederação de Natação e direi sua categoria!!!")

atual = date.today().year

nome = input("Olá, qual seu nome? ")
ano = int(input(f"Tudo bem, {nome}, em que ano você nasceu? "))

idade = atual - ano

if idade < 0:
    print("Você ainda não nasceu!")
elif idade > 120:
    print("Digite uma idade válida!")
elif idade <= 9:
    print(f"{nome}, você pertence à categoria \033[1;34mMIRIM\033[0m")
elif idade <= 14:
    print(f"{nome}, você pertence à categoria \033[1;34mINFANTIL\033[0m")
elif idade <= 19:
    print(f"{nome}, você pertence à categoria \033[1;34mJUNIOR\033[0m")
elif idade <= 20:
    print(f"{nome}, você pertence à categoria \033[1;34mSÊNIOR\033[0m")
else:
    print(f"{nome}, você pertence à categoria \033[1;34mMASTER\033[0m")
