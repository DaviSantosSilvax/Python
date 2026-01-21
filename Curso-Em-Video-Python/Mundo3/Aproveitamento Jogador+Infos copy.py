import time 
print("\033[3;35mMe Diga Quantas Partidas Um Jogador Teve e Direi o Aproveitamento Dele!!!\033[0;37m")
jogadores = []
cod = 0
def linha():
    print("\033[34m=-"*20)


while True:
    total = 0
    gols = []
    mediag = 0
    nome = str(input("\033[35mQual Nome Do Seu Jogador?\033[33m "))
    while not nome.replace(" ", "").isalpha():
        nome = str(input("\033[35mQual Nome Do Seu Jogador?\033[33m "))
    while True:
        np = input(f"\033[35mQuantas Partidas Teve o {nome}?\033[33m ")
        if np.isdigit():
            np = int(np)
            break
        print("\033[31mDigite Apenas Números Válidos!!")
    if np == 0:
        print("\033[31mJogador Nunca Jogou!!")
        continue
    for p in range(1, np+1):
        while True:
            gol = input(f"\033[35mQuantos Gols {nome} fez na {p} Partida?\033[33m ")
            if gol.isdigit():
                gol = int(gol)
                break
            print("\033[31mDigite Números Válidos:\033[33m ")

        mediag += gol
        total += gol
        gols.append(gol)
    
    mediag /= np
    cod += 1
    jogador = {"Cod": cod, "Nome": nome, "Gols": gols, "Total": total, "Media De Gols": mediag}

    jogadores.append(jogador)


    c = str(input("\033[35mSe Quiser Parar Digite [ \033[33mN\033[35m ]: ")).lower()
    if c == "n":
        break

print(f"\033[33m{'Cod':>5}{'Nome':>12}{'Gols':>15}->{'Total:':<10}{'Media De Gols':<10}")
linha()

for i in jogadores:
    print(f"\033[32m{i['Cod']:>5}{i['Nome']:>10}{str(i['Gols']):>20}{i['Total']:<10}{i['Media De Gols']:<8.1f}")



linha()

while True:
    linha()
    Codigo = input("\033[35mMostrar Dados De Qual Jogador?[\033[33m0\033[35m] Para Parar\033[33m ")
    while not Codigo.isdigit():
            Codigo = input("\033[35Digite Apenas Números!!\033[33m ")      
    if Codigo == "0":
            break
    
    Codigo = int(Codigo)
    encontrado = False
    
    for i in jogadores:
        if Codigo == i["Cod"]:
            encontrado = True

            for k, v in i.items():
                print(f"\033[35mO Campo \033[1;32m{k}\033[0;35m Tem Valor: \033[1;32m{v}\033[0;35m")
            linha()
            time.sleep(0.2)
            for e,g in enumerate(i["Gols"]):
                print(f"\033[35mNa Partida \033[32m{e+1}\033[35m, Fez \033[32m{g}\033[35m Gol(s)")
                time.sleep(0.6)

            linha()
            print(
    f"\033[35mForam O Total De \033[32m{i['Total']} Gol(s) "
    f"\033[35m Em \033[32m{len(i['Gols'])} Partidas"
    f"\033[35m Ficando A Média De \033[32m{i['Media De Gols']:.1f}\033[35m !!!"
)

    if not encontrado:
        print("\033[31mJogador Não Registrado!!")

            
            