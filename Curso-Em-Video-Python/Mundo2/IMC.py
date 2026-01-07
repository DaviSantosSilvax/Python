print("\033[0;35;40mFarei seu IMC e irei te categorizar\033[m")

nome = input("Qual seu nome? ")
altura = float(input(f"Ok {nome}, qual sua altura (em metros)? "))
peso = float(input("E quanto você está pesando (em kg)? "))

imc = peso / (altura ** 2)
print(imc)
if imc < 18.5:
    print("Você está \033[0;31;40mabaixo do peso!\033[m")
elif imc < 25:
    print("Você está no \033[0;32;40mpeso ideal!\033[m")
elif imc < 30:
    print("Você está em \033[0;35;40mSobrepeso!\033[m")
elif imc < 40:
    print("Você está em \033[0;33;40mObesidade!\033[m")
else:
    print("Você está em \033[0;31;40mObesidade Mórbida!\033[m")
