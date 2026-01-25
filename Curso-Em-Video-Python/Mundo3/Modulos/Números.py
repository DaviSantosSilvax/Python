import Uteis

num = int(input("\033[35mDigite Um Valor:\033[33m "))
fat = Uteis.fatorial(num)
dobro = Uteis.dobro(num)
triplo = Uteis.triplo(num)
print(f"\033[35mO Fatorial De \033[32m{num}\033[35m é \033[32m{fat}\033[35m")
print(f"\033[35mO Dobro De \033[32m{num}\033[35m é \033[32m{dobro}\033[35m")
print(f"\033[35mO Triplo De \033[32m{num}\033[35m é \033[32m{triplo}\033[35m")