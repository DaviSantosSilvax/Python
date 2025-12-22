print("Irei calcular o preço de uma passagem para sua viagem")
print("Cada Km de sua viagem custará R$0,50 \nSe sua viagem for mais de 200KM iremos cobrar R$0,45 por KM!!!")


distancia = int(input("Quantos Km de distância tem sua viagem?"))
km1 = distancia * 0.50
km2 = distancia * 0.45
desconto = km1 - km2


if distancia <= 200:
    print(f"Será cobrada sua passagem de R${km1}! ")

else:
    print("verificamos que sua viagem é acima de 200KM!! ")
    print(f"Será cobrada sua passagem de {km2} já com desconto!!! ")
    print(f"o desconto em sua passagem foi de R${desconto}!! Parabéns. ")