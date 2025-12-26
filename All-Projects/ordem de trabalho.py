import random
print("Um professor tem que sortear 4 grupos de alunos para apresentar seu trabalho")
gp1 = str(input("me diga o nome do representante do primeiro grupo: "))
gp2 = str(input("me diga o nome do representante do segundo grupo: "))
gp3 = str(input("me diga o nome do representante do terceiro grupo: "))
gp4 = str(input("me diga o nome do representante do quarto grupo: "))

grupos = [gp1, gp2, gp3, gp4]
random.shuffle(grupos)

print("A ordem dos grupos ficou {}" .format(grupos))