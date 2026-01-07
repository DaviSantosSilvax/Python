print("\033[35mIrei Te Mostrar Os Primeiros N Termos Da \033[32mSequencia De Fibonacci\033[35m")
n = int(input("Me Diga a Quantidade De Números Que Deseja Saber Da Sequencia: \033[32m"))
print("\033[36m_-_-"*20)
c = 2
t1 = 0
t2 = 1
print(f"\033[33m{t1} -> {t2} ",end="")
while c < n:
    t3 = t1 + t2
    print(f"-> {t3} ",end="")
    t1 = t2
    t2 = t3
    c+= 1
print("\n\033[1;31m..::Fim::..\033[0;37m")


