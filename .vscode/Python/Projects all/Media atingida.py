print("Direi pela sua média das provas se passou ou reprovou!!!")

nome = input("Olá, qual seu nome? ")
a1 = float(input(f"Tudo bem, {nome}, qual sua primeira nota? "))
a2 = float(input("E qual sua segunda nota? "))

media = (a1 + a2) / 2

if media >= 7.0:
    print("\033[0;32;40mPARABÉNS!!!\033[0;37;40m você foi \033[0;32;40maprovado\033[0;37;40m!!!")

elif media < 5.0:
    print("\033[0;31;40mVocê foi reprovado!!!!\033[0;37;40m")

elif 5.0 <= media <= 6.9:
    print("Você está de \033[0;33;40mRecuperação!!!\033[0;37;40m")
