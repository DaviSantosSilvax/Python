print("\033[35mIrei Ler o Primeiro Termo e Razão Da Sua P.A e Mostrar Os 10 Primeiros Termos!!") 
t = int(input("Me Diga o Primeiro Termo:\033[36m "))
r = int(input("\033[35mMe Diga a Razão:\033[36m "))
rep = 10
to = 0
while t < 0:
    t = int(input("Digite Um Valor Válido: "))
while r <= 0:
    r = int(input("Digite Um Valor Válido: "))
while rep > 0:
    print(t)
    to += t
    t +=r
    rep -= 1

print(f"\033[35mA Soma Dos \033[32m10 Primeiros Termos\033[35m é {to}")