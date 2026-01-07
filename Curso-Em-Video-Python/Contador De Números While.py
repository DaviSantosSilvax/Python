print("\033[35mContador de Números Inteiros e Soma Final Entre Eles!!!")
n = 0
c = 0
s = 0
while True:
    n = int(input("Diga Um Número e \033[32m[999]\033[35m Para Finalizar o Programa:"))
    if n == 999:
        print("\033[35m..::\033[1;31mPrograma Finalizado\033[35m::..")
        break
    c += 1
    s += n
print(f"Seu Programa Possuiu \033[32m{c} \033[35mValores e o Total de  \033[32m{s}")
