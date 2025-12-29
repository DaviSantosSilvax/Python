import time
print("\033[0;35;40mIrei Te dizer Os \033[01;32;40mNúmeros Impares\033[0;35;40m que são \033[01;32;40mMúltiplos De Três\033[0;35;40m entre \033[1;32;40m1 Até 500\033[0;35;40m!!!\033[0;37;40m")
input("\033[0;35;40mAperte \033[01;32;40mENTER\033[0;35;40m Para Visualizar!!!\033[0;37;40m")
s = 0
for i in range(3, 501, 6):
    print(i)
    time.sleep(0.1)
    s += i
print(f"\033[0;35;40mA Soma Dos Números De \033[01;34;40m1 à 500\033[0;35;40m, \033[1;34;40mImpares e Múltiplos De Três\033[0;35;40m é: \033[1;32;40m {s}!!\033[0;37;40m")