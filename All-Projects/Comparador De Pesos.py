print("\033[0;35;40mIrei Comparar O Peso De Cinco Pessoas e Direi O Maior e o Menor!!!\033[0;37;40m")
p1 = 1
p2 = float("inf")
for i in range(1, 6):
    p = float(input("\033[0;35;40mMe Diga o Peso Desta Pessoa: \033[0;37;40m"))
    if p < p2:
        p2 = p
    if p > p1:
        p1 = p
print(f"O maior peso é {p1} e o menor é {p2}")