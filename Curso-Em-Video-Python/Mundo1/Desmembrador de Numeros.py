print("Desmembro Seus números!!!")

numero = str(input("Me Diga Um Número inteiro Entre 0 à 9999 e Direi Seus Digitos Separadamente "))
numero = numero.zfill(4)

unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

print(f""""Unidade:{unidade}
Dezana:{dezena}
Centena:{centena}
Milhar:{milhar}
""")

