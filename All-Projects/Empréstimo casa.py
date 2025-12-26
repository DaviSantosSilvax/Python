import time
print("Aprovar Empréstimo para casa")

time.sleep(1)
print("O valor da sua prestação não poderá exceder 30% do seu sálario")
time.sleep(1)
valor = int(input("Qual o valor da casa que planeja comprar? "))
salario = int(input("Qual seu Salário Mensal?? "))
tempo = int(input("Em quantos anos você planeja pagar pela casa? "))
meses = tempo * 12
prestacao = valor / meses

if prestacao > salario * 0.30:
    print("Desculpe, Não será possivel aceitar este acordo!!!")

else:
    print("Muito bem!!! Podemos fechar este acordo!!!")