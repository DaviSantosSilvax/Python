print("Darei um aumento do seu salario")
print("Se seu salario for superior a R$1.250 você terá de 10% \nPara inferiores ou iguais, o aumento é de 15%")

salario = float(input("Qual seu salário??: "))

if salario > 1250:
    salario_atual = salario + (salario * 0.10)
    print(f"Seu salario atual será de R${salario_atual:.2f} ")

else:
    salario_atual = salario + (salario * 0.15)
    print(f"seu salario atual será de R${salario_atual:.2f}")