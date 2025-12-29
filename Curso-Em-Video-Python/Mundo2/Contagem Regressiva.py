import time
vermelho = "\033[01;31;40m"
padrão = "\033[00;37;40m"
roxo = "\033[00;35;40m"
print(f'{roxo}Vamos Lá, Escreva {vermelho}"BOOM"{roxo} e comece a contagem para os fogos de artificio!!!{padrão}'.title())
input(f"Pressione {vermelho}ENTER{padrão} Para Começar A Contagem!!!")
for b in range(10, 0, -1):
    print(b)
    time.sleep(1)
print(f"{vermelho}KABUM!!!!{padrão}")
print(f"{vermelho}POWWW KABUM!!!!{padrão}")
print(f"{vermelho}PUW PUW KABUW!!!!{padrão}")
