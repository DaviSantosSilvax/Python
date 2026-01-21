import time
print("\033[3;35mVou Mostrar Os Vinte Primeiros Colocados Da Tabela Do Brasileirão, \nVou Mostrar Os 5 Primeiros Colocados, \nOs Últimos Colocados Da Tabela, \nUma lista Com Os Times Em Ordem Alfabética, \nTambém Em que Ordem Está o Botafogo\033[0;35m")
bra = (
    "Flamengo",        # 1º
    "Palmeiras",       # 2º
    "Cruzeiro",        # 3º
    "Mirassol",        # 4º
    "Fluminense",      # 5º
    "Botafogo",        # 6º
    "Bahia",           # 7º
    "São Paulo",       # 8º
    "Grêmio",          # 9º
    "Red Bull Bragantino",  # 10º
    "Atlético Mineiro",     # 11º
    "Santos",              # 12º
    "Corinthians",         # 13º
    "Vasco da Gama",       # 14º
    "Vitória",            # 15º
    "Internacional",      # 16º
    "Ceará",              # 17º
    "Fortaleza",          # 18º
    "Juventude",          # 19º
    "Sport"               # 20º
)
time.sleep(2.5)
print("\033[0;34m==="*20)
time.sleep(1)
print(f"\033[36mOs Vinte Primeiros Colocados Do Brasileirão Da Série A é\n{bra}")
time.sleep(0.5)
print("\033[0;34m==="*20)
time.sleep(1)
print(f"\033[36mOs 5 Primeiros Colocados Do Brasileirão Da Série A São\n{bra[0: 5]}")
time.sleep(0.5)
print("\033[0;34m==="*20)
time.sleep(1)
print(f"\033[36mOs Ultimos 5 Colocados Da Tabela Do Brasileirão Da Série A São\n {bra[15: ]}")
time.sleep(0.5)
print("\033[0;34m==="*20)
time.sleep(1)
print(f"\033[36mA Tabela Em Ordem Alfabética Fica Da Seguinte Forma:\n {sorted(bra)}")
time.sleep(0.5)
print("\033[0;34m==="*20)
time.sleep(1)
print(f"\033[36mO BotaFogo Está Na {bra.index("Botafogo")}° Posição")
time.sleep(0.5)
print("\033[0;34m==="*20)
