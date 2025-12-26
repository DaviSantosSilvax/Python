print("Jogo da adivinhação Básico")
n = 3

while True:
    numero = int(input("Tente acertar o número que estou pensando de 1 a 5 (ou 0 para sair): "))
    
    if numero == 0:
        print("Jogo encerrado!")
        break  

    elif numero == n:
        print("Parabéns, você acertou meu número!!!!")
        break  
    else:
        print("Ainda não é este, tente novamente!!!")
