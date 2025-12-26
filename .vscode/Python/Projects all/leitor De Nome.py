print("Digo Seu Primeiro e Último nome separadamente.")

nome = str(input("Diga Seu nome e direi seu primeiro e último separados").title())

fatia = nome.split()
nomep = fatia[0]
nomeu = fatia[-1]

print(f"Seu primeiro nome é {nomep} e seu ultimo nome é {nomeu}".title())