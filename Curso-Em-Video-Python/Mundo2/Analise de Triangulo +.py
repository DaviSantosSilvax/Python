print("Irei analisar suas 3 retas e dizer se elas podem formar um triângulo e também o tipo de triângulo")

a1 = int(input("Olá, me diga a primeira reta: "))
a2 = int(input("Olá, me diga a segunda reta: "))
a3 = int(input("Olá, me diga a terceira reta: "))

if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
    print("\033[0;32;40mSuas retas podem formar um triângulo!\033[m")

    if a1 == a2 == a3:
        print("Você possui um \033[0;34;40mTriângulo Equilátero\033[m")
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print("Você possui um \033[0;33;40mTriângulo Isósceles\033[m")
    else:
        print("Você possui um \033[0;36;40mTriângulo Escaleno\033[m")
else:
    print("\033[0;31;40mImpossível formar um triângulo com as retas apresentadas!\033[m")

