from Modulos import moeda

print("\033[35mIrei Usar Modulos Para Calcular Seu Dinheiro De Forma Basica!")

p = float(input("\033[35mDigite o Preço: R$\033[33m "))
print(f"\033[35mA Metade De {moeda.moeda(p)} é \033[32m{moeda.moeda(moeda.metade(p))}")
print(f"\033[35mO Dobro De {moeda.moeda(p)} é \033[32m{moeda.moeda(moeda.dobro(p))}")
print(f"\033[35mAumentando 10%, Temos \033[32m{moeda.moeda(moeda.aumentar(p, 10))}")
print(f"\033[35mReduzindo 13%, Temos \033[32m{moeda.moeda(moeda.diminuir(p, 13))}")