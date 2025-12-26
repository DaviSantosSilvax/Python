import time
print("analiso seu nome")
time.sleep(1)
print("direi seu nome com todas letras maiúsculas")
time.sleep(1)
print("seu nome com todas letras minúsculas")
time.sleep(1)
print("quantas letras ao todo")
time.sleep(1)
print("quantas letras tem seu primeiro nome")
time.sleep(1)
nome = str(input("vamos começar??? Me diga seu nome completo!!! "))

NOME = nome.upper()
Nome = nome.lower()
quantidade = nome.replace(" ", "")
numero = len(quantidade)
fatia = nome.split()


print(f"""
Seu nome com todas letras maiúsculas fica {NOME}, 
Seu nome com todas letras minúsculas fica {Nome},
Seu nome tem exatamente {numero} letras,
Seu primeiro nome é {fatia[0]}. """)

