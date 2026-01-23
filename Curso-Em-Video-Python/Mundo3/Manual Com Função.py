import time
def divisão(msg):
def ajuda():
    while True:
        print("\033[34m=-"*13)
        print("\033[37;43m Sistema De Ajuda PyHELP\033[37;40m")
        print("\033[34m=-"*13)
        n = (input("\033[35mFunção Ou Biblioteca:\033[33m ")).lower()
        if n == "fim":
            print("\033[31mFim")
            break
        else:
            time.sleep(1)
            print("\033[35m=-"*20)
            print(f"\033[35;44m Acessando o Manual Do Comando \033[01;34;45m{n}\033[0;37;40m")
            print("\033[35m=-\033[34m"*20)
            time.sleep(1)
            help(n)
            continue

ajuda()