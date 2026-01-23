print("\033[35mIrei Fazer Uma Função Que Dirá Qual Nome Do Seu Jogador e Quantos Gols Ele Fez.")
def ficha():
    nome = input("Qual Nome Do Seu Jogador? ").strip()
    if not nome:
        nome = "<desconhecido>"
    gols = input("Quantos Gols Este Jogador Fez? ").strip()
    while not gols.isdigit() and gols != "":
        gols = input("Quantos Gols Este Jogador Fez? ").strip()
    if not gols:
        gols = 0
    else:
        gols = int(gols)
    print(f"O Jogador {nome} Fez {gols} Gol(s) No Campeonato.")
 

ficha()