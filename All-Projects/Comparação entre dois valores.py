print("\033[01;35;40mComparação Entre Dois valores Inteiros\033[0;37;40m")

n1 = int(input("\033[0;35;40mDigite O \033[0;32;40mPrimeiro\033[0;35;40m Valor!!\033[0;37;40m"))
n2 = int(input("\033[0;35;40mDigite O \033[0;32;40mSegundo\033[0;35;40m Valor!!\033[0;37;40m"))

if n1 > n2:
    print(f"\033[0;35;40mO \033[1;32;40mPrimeiro Valor\033[0;35;40m é maior, \033[0;32;40m{n1}\033[0;35;40m é maior que \033[0;31;40m{n2}\033[0;37;40m")

elif n2 > n1:
    print(f"\033[0;35;40mO \033[1;32;40mSegundo Valor\033[0;35;40m é maior, \033[0;32;40m{n2}\033[0;35;40m é maior que \033[0;31;40m{n1}\033[0;37;40m")
elif n1 == n2:
    print(f"\033[01;32;40mNão existe Valor Maior ")
    print(f"\033[01;35;40mOs Valores\033[1;32;40m {n1}\033[0;35;40m e \033[01;32;40m{n2}\033[0;33;40m São Iguais!!!\033[0;37;40m")