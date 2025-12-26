from datetime import date

print("Você está na confederação de Natação e direi sua categoria!!!")

atual = date.today().year

nome = input("Olá, qual seu nome? ")
ano = int(input(f"Tudo bem, \033[1;34;37m{nome}\033[0;30;37m, em que ano você nasceu? "))

idade = atual - ano

if idade < 0:
    print("Você ainda não nasceu!")
elif idade <= 9:
    print(f"{nome}, você pertence à categoria \033[1;34;37mMIRIM\033[0;30;37m")
elif idade <= 14:
    print(f"{nome}, você pertence à categoria \033[1;34;37mINFANTIL\033[0;30;37m")
elif idade <= 19:
    print(f"{nome}, você pertence à categoria \033[1;34;37mJUNIOR\033[0;30;37m")
elif idade <= 20:
    print(f"{nome}, você pertence à categoria \033[1;34;37mSÊNIOR\033[0;30;37m")
else:
    print(f"{nome}, você pertence à categoria \033[1;34;37mMASTER\033[0;30;37m")
