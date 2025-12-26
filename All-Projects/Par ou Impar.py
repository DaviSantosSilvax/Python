print("Mostro se um número é Par ou Impar")

while True:
    numero = int(input("Me diga um número e direi se ele é Par ou Impar!!!! 0 para encerrar: "))
    
    if numero == 0:
        print("..::Programa Encerrado::..")
        break

    
    elif numero % 2 == 0:
        print("Seu número é par!!!")



    else:
        print("Seu número é impar!!!")
