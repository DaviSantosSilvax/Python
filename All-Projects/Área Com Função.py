print("\033[35mIrei Mostrar A Área De Um Terreno Que Você Irá Dizer a Largura e Comprimento!!")

def area(l, c):
    a = l * c
    print(f"\033[35mA Área Do Seu Terreno é De \033[34m{l}\033[35mX\033[34m{c}\033[35m é De \033[32m{a}m²\033[35m!!!")

largura = float(input("\033[35mLargura (m):\033[33m "))
comprimento = float(input("\033[35mComprimento (m):\033[33m "))
area(largura, comprimento)
