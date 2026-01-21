import time
print("\033[35mIrei Fazer Com Que Sejam Analisados Varios Valores e Mostrar o Maior!!")
print("\033[35m=-"*20)
def maior(*n):
    if not n:
        print("\033[35mAnalisando Os Valores Passados...")
        print("\033[35mForam Informados \033[31m0 \033[35mValores.")
        print("\033[35mO Maior Valor Informado Foi \033[31m0\033[35m.")
        return
    for i in n:
        print(f"\033[32m{i}", end=", ",flush=True)
        time.sleep(1)
    print(f"\033[35m Foram Informados \033[32m{len(n)}\033[35m Ao Todo.")
    print()
    print(f"\033[35mO Maior Valor Informado Foi \033[32m{max(n)}\033[35m.")
    print("\033[35m=-"*20)


time.sleep(0.5)
maior(2, 9, 4, 5, 7, 1)
time.sleep(0.5)
maior(4,7, 0)
time.sleep(0.5)
maior(1, 2)
time.sleep(0.5)
maior(6)
time.sleep(0.5)