import time
print("\033[0;35;40mBem Vindo A Calculadora!!")
time.sleep(0.25)
n1 = int(input("\033[33mMe Diga O Primeiro Valor:\033[0;32;40m "))
time.sleep(0.25)
n2 = int(input("\033[0;33;40mMe Diga O Segundo Valor:\033[0;32;40m "))

opc = 0
while opc != 5:
    print(
    "\033[1;32;40m[1]\033[0;35;40m Somar\n"
    "\033[1;32;40m[2]\033[0;35;40m Multiplicar\n"
    "\033[1;32;40m[3]\033[0;35;40m Maior\n"
    "\033[1;32;40m[4]\033[0;35;40m Novos Números\n"
    "\033[1;32;40m[5]\033[0;35;40m Sair do Programa\033[0;37;40m")
    opc = input("\033[0;35;40mEscolha Uma das Opções acima entre 1-5:\033[0;32m ")
    time.sleep(0.20)

    if not opc.isdigit():
        print("Opção inválida! Digite apenas números.")
        continue

    opc = int(opc)

    if opc == 1:
        print(f"{n1} + {n2} = {n1+n2}")
    elif opc == 2:
        print(f"{n1} X {n2} = {n1*n2}")
    elif opc == 3:
        if n1 > n2:
 
            print(f"O Maior Valor é {n1}!")
        elif n2 > n1:
            print(f"O Maior Valor é {n2}!")
        else:
            print("Ambos Os Valores São Iguais!!!")
    elif opc == 4:
        n1 = int(input("\033[33mMe Diga O Primeiro Valor:\033[32m "))
        time.sleep(0.2)
        n2 = int(input("\033[33mMe Diga O Segundo Valor:\033[32m "))
    elif opc == 5:
        print("\033[1;34m....::::\033[31mSaindo Do Programa!!!\033[32m::::....\033[0;37m")
    else:
        print("\033[1;31mOpção Invalida!!! Insira Uma opção Válida!!!\033[0;32;40m")   


    
