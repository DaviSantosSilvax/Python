print("\033[0;35;40mIrei Dizer Quantas Pessoas Tem Idade acima ou Igual à 20 Anos de Idade!!\033[0;37;40m")
s = 0
for i in range(1,8):
    n = int(input("\033[1;35;40mQual Idade Desta Pessoa?\033[0;37;40m "))
    if n >= 20:
        s += 1
print(f"\033[0;32;40m{s}\033[0;35;40m Pessoas Tem Maioridade Penal!!!\033[0;37;40m")
