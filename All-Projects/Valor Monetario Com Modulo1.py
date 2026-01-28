from Modulos import moeda

print("\033[35mIrei Usar Modulos Para Calcular Seu Dinheiro De Forma Basica!")

p = float(input("\033[35mDigite o Preço: R$\033[33m "))
print(f"\033[35mA Metade De {p} é \033[32m{moeda.metade(p)}")
print(f"\033[35mO Dobro De {p} é \033[32m{moeda.dobro(p)}")
print(f"\033[35mAumentando 10%, Temos \033[32m{moeda.aumentar(p, 10)}")
print(f"\033[35mReduzindo 13%, Temos \033[32m{moeda.diminuir(p, 13)}")