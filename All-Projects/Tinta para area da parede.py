
print("Digite a altura e largura da sua parede que direi a area dela e quanta tinta será necessaria \n cada litro de tinta pinta 2 metro²")

Pa = float(input("Qual altura da sua parede? "))
Pl = float(input("Qual largura da sua parede? "))
a = Pa * Pl
t = int(a // 2)




print(f"Sua parede tem {a} de area, então será necessario {t} baldes de tinta")