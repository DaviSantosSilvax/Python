print("Radar de velocidade")
print("Este Radar de velocidade é até 80Km/h!!!")

radar = 80



while True:
    velocidade = int(input("Qual velocidade estava seu carro? Se não tiver carro digite  ''0'' "))
    multa = (velocidade - 80) * 7

    if velocidade == 0:
        print("Encerrando radar")
        break
   


    elif velocidade > radar:
        print("Você Foi multado por passar acima do limite!!!")
        print(f"Sua multa é de R${multa}!!")
    
    else:
        print("Você não levou multa!! parabéns por andar na Lei!")