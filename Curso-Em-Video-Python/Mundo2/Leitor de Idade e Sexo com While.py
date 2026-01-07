print("\033[3;35mIrei Ler Idade, Sexo Dos Usuários e No Final Dizer\n\033[0;32mQuanta Pessoas São maiores De 18 anos\nQuantos Homens Cadastrados e\nQuantas Mulheres Tem Menos De 20 Anos!!!")
f = True
maiores = 0
homem = 0
m20 = 0
while f:
    print("\033[35m=="*20)
    idade = int(input("\033[35mQual Sua Idade?\033[33m "))
    while idade < 0:
        idade = int(input("\033[35mDigite Uma Idade Válida:\033[33m"))
    if idade >= 18:
        maiores += 1
    
    sexo = input("\033[35mQual Seu Sexo? \033[1;32m[H] \033[0;35mPara Homem e \033[1;32m[F]\033[0;35m Para Mulher:\033[33m ").lower()
    while sexo not in("h", "f"):
        sexo = input("\033[35mDigite Um Sexo Válido\033[1;32m[H]\033[0;35m Ou \033[1;32m[F]:\033[0;33m")
    if sexo == "h":
        homem += 1
    if sexo == "f" and idade < 20:
        m20 += 1
    
    c = input("\033[35mSe Deseja Continuar, Digite \033[32m[S]\033[35m Se Deseja Finalizar Digite \033[31m[N]:\033[33m ").lower()
    while c not in ("s", "n"):
        c = input("\033[35mDigite \033[32m[S]\033[35m ou \033[31m[N]:\033[33m").lower()
    if c == "s":
        continue
    elif c == "n":
        f = False
        break
print("\033[1;31m..::\033[0;33mFim Do Programa\033[1;31m::..\033[0;35m")
print(f"\033[35mForam Cadastradas \033[1;32m{maiores}\033[0;35m Pessoas Maiores de 18 Anos!!!")
print(f"\033[35mForam Cadastradas \033[1;32m{homem}\033[0;35m Homens!!!")
print(f"\033[35mForam Cadastradas \033[1;32m{m20}\033[0;35m Mulheres Com Idade Menor Que 20 Anos!!!")
print("\033[31m==\033[0;37m"*20)

