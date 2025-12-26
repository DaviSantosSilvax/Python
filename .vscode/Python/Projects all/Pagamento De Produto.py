print("Direi quanto você pagará em um produto conforme a forma de pagamento")

preco = float(input("Qual o \033[0;33;40mpreço\033[0;37;40m do produto? R$ "))

print("1 - À vista dinheiro/cheque (10% de desconto)")
print("2 - À vista no cartão (5% de desconto)")
print("3 - Até 2x no cartão (preço normal)")
print("4 - 3x ou mais no cartão (20% de juros)")
print("0 - Sair")

while True:
    opc = int(input("Escolha uma opção: "))

    if opc == 0:
        print("..:: FIM DO PROGRAMA ::..")
        break
    elif opc == 1:
        total = preco * 0.90
    elif opc == 2:
        total = preco * 0.95
    elif opc == 3:
        total = preco
    elif opc == 4:
        total = preco * 1.20
    else:
        print("Opção inválida! Tente novamente.")
        continue

    print(f"\033[0;32;40mSeu produto ficou em R$ {total:.2f}\033[0;33;40m")
    break
