print("\033[01;35;40mConversor De Bases Numéricas\033[0;37;40m")

n = int(input("\033[0;35;40mDigite Um Número Inteiro:\033[0;37;40m"))

while True:
    print("\033[1;33;40m1\033[0;35;40m - Converter Para \033[1;32;40mBINÁRIO\033[0;37;40m")
    print("\033[1;33;40m2\033[0;35;40m - Converter Para \033[1;32;40mOCTAL\033[0;37;40m")
    print("\033[1;33;40m3\033[0;35;40m - Converter Para \033[1;32;40mHEXADECIMAL\033[0;37;40m")
    print("\033[1;33;40m0\033[0;35;40m - Para \033[1;31;40mSAIR\033[0;37;40m")
    opc = int(input("\033[0;35;40mEscolha Uma Base De Conversão\033[0;37;40m"))

    
    if opc == 0:
        print("\033[0;36;40m..::\033[0;31;40mPrograma Encerrado\033[0;36;40m::..\033[0;37;40m")
        exit()
    elif opc == 1:
        print(f"\033[0;32;40m{n}\033[0;35;40m Convertido para \033[0;32;40mBinario\033[0;35;40m é \033[0;32;40m{bin(n)}\033[0;37;40m")

    elif opc == 2:
        print(f"\033[0;32;40m{n}\033[0;35;40m Convertido para \033[0;32;40mOctal\033[0;35;40m é \033[0;32;40m{oct(n)}\033[0;37;40m")

    elif opc == 3:
        print(f"\033[0;32;40m{n}\033[0;35;40m Convertido para \033[0;32;40mHexadecimal\033[0;35;40m é \033[0;32;40m{hex(n)}\033[0;37;40m")

    else:
        print("\033[01;31;40mNúmero inválido\033[0;37;40m")