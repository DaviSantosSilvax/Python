print("\033[0;35;40mBem Vindo A Calculadora!!")
n1 = int(input("Me Diga O Primeiro Valor:\033[0;32;40m "))
n2 = int(input("\033[0;35;40mMe Diga O Segundo Valor:\033[0;32;40m "))

opc = 0
while opc != 5:
    print(
    "\033[1;32;40m[1]\033[0;35;40m Somar\n"
    "\033[1;32;40m[2]\033[0;35;40m Multiplicar\n"
    "\033[1;32;40m[3]\033[0;35;40m Maior\n"
    "\033[1;32;40m[4]\033[0;35;40m Novos Números\n"
    "\033[1;32;40m[5]\033[0;35;40m Sair do Programa\033[0;37;40m")
    try:
        opc = int(input("Escolha Uma das Opções acima entre 1-5: "))
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
        n1 = int(input("Me Diga O Primeiro Valor:\033[0;32;40m "))
        n2 = int(input("\033[0;35;40mMe Diga O Segundo Valor:\033[0;32;40m "))
    else:
        print("Opção Invalida!!! Insira Uma opção Válida!!!")   


    
