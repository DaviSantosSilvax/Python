print("Direi se suas três retas podem ser um triângulo")


lado1 = int(input("Me diga o primeiro lado do seu triangulo: "))
lado2 = int(input("Me diga o segundo lado do seu triangulo: "))
lado3 = int(input("Me diga o terceiro lado do seu triangulo: "))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print("Suas três retas podem ser um triângulo!!!")

else:
    print("Suas retas não podem ser triangulos")