import time
print("Irei Mostrar A Tabuada Do Número Que Você Escolher!!!")

n = int(input("\033[0;35;40mDigite um Número e Direi a Tabuada deste Número de \033[1;32;40m1 À 10\033[0;37;40m "))
print(f"\033[0;35;40mTabuada de \033[1;32;40m{n}\033[0;35;40m:\033[0;37;40m")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print("\033[0;33;40m..::\033[0;32;40mFim do Programa\033[0;33;40m::..\033[0;37;40m")