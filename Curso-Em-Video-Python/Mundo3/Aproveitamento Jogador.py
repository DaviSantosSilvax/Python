print("\033[3;35mMe Diga Quantas Partidas Um Jogador Teve e Direi o Aproveitamento Dele!!!\033[0;37m")
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
    exit()
for p in range(1, np+1):
    while True:
        gol = input(f"\033[35mQuantos Gols {nome} fez na {p} Partida?\033[33m ")
        if gol.isdigit():
            gol = int(gol)
            break
        print("\033[31mDigite Números Válidos:\033[33m ")
    mediag += gol
    gols.append(gol)

print("\033[36m=-"*20)
dic = {"Nome": nome, "Gols": gols, "Total": mediag}
mediag /= np
dic["Media"] = mediag

for k, i in dic.items():
    print(f"\033[35mO Campo \033[1;32m{k}\033[0;35m Tem Valor: \033[1;32m{i}\033[0;35m")

print("\033[36m=-"*20)

for i,g in enumerate(gols):
    print(f"\033[35mNa Partida {i+1}, Fez \033[32m{g}\033[35m Gol(s)")

print(f"\033[35mForam O Total De \033[32m{dic['Total']} Gol(s)\033[35m Em \033[32m{np} Partidas\033[35m Ficando A Média De \033[32m{mediag:.1f}\033[35m !!! ")

print("\033[36m=-"*20)