
def erro_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("\033[31mDigite Um Valor Válido!!!")
lista = []
pares = []
impares = []
f = True
while f:
    l = erro_int("\033[35mDigite Um Número: \033[33m")
    if l in lista: 
        print("\033[31mNúmero Já Inserido!!")
    else:
        lista.append(l)
        if l % 2 == 0:
            pares.append(l)
        else:
            impares.append(l)
    c = input("\033[35mDeseja Continuar? Digite [\033[31mN\033[35m] Para Finalizar:\033[33m ").lower()
    if c == "n":
        f = False
        
print("\033[36mxX"*20)
print(f"\033[35mSua Lista De Números Gerais é: \033[32m{sorted(lista)}")
print("\033[36mxX"*20)
print(f"\033[35mSua Lista De Números pares é: \033[32m{sorted(pares)}")
print("\033[36mxX"*20)
print(f"\033[35mSua Lista De Números Impares é: \033[32m{sorted(impares)}")