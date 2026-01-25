import time
def divisão(msg):
    print(f"\033[35m{"-"*(len(msg)+2)}")
    print(f"\033[34m {msg}")
    print(f"\033[35m{"-"*(len(msg)+2)}")
def ajuda():
    while True:
        divisão(msg="Sistema De Ajuda PyHELP")
        n = (input("\033[35mFunção Ou Biblioteca:\033[33m ")).lower()
        if n == "fim":
            print("\033[31mFim")
            break
        else:
            time.sleep(1)
            divisão(f'Acessando o Manual Do Comando \033[01;34;45m{n}\033[0;35;40m')
            time.sleep(1)
            help(n)
            continue

ajuda()