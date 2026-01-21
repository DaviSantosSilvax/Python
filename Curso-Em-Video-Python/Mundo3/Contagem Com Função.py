import time
print("\033[35mIrei Primeiro De 1 em 1 Contar De 1 Até 10, De 10 Até 1 e Em Seguida Você Irá Personalizar a Contagem!!")
def contagem():
    time.sleep(0.5)
    print("\033[34m=-"*20)
    print("\033[35mContagem De 0 Até 10 De 1 Em 1")
    for i in range(1, 11):
        print(f"\033[36m{i}", end=" ", flush=True)
        time.sleep(0.5)
    print()
    print("\033[34m=-"*20)
    print("Contagem De 10 Até 0 De 2 Em 2")
    for i in range(10, -1, -2):
        print(f"\033[36m{i}", end=" ", flush=True)
        time.sleep(0.5)
    time.sleep(0.5)
    print()
    print("\033[34m=-"*20)
    print("\033[35mSua Vez De Fazer Uma Contagem Personalizada!!!")
    p = int(input("\033[35mInicio:\033[33m "))
    u = int(input("\033[35mFim:\033[33m "))
    d = int(input("\033[35mPasso:\033[33m "))
    if d == 0:
        d = 1
    elif d < 0:
        d = -d
    if p <=  u:
        print(f"\033[35mContagem De \033[32m{p}\033[35m Até \033[32m{u}\033[35m De \033[32m{d}\033[35m Em \033[32m{d}\033[35m")
        for i in range(p, u+1, d):

            print(f"\033[36m{i}", end=" ", flush=True)
            time.sleep(0.5)
    elif p > u:
        print(f"\033[35mContagem De \033[32m{p}\033[35m Até \033[32m{u}\033[35m De \033[32m{d}\033[35m Em \033[32m{d}\033[35m")
        for i in range(p, u-1, -d):
            print(f"\033[36m{i}", end=" ", flush=True)
            time.sleep(0.5)
    print("\033[31mFim!\033[37m")

contagem()