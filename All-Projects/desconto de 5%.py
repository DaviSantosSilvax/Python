print("Me diga seu produto e quanto ele custa, direi quanto ele ficaria com desconto de 5% ")
produto = input("Qual produto? ")
preço = int(input("Qual preço do(a){} ".format(produto)))

porcento = preço // 5
desconto = preço - porcento

print(f"O preço do {produto} com desconto de 5% é de {desconto}")

  