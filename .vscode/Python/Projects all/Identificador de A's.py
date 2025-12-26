print('identificarei "A" em sua frase'.title())

frase = str(input('Diga Uma Frase e analisarei Os "A" Nela: '))


frases = frase.lower().replace(" ", "")
frasec = frases.count('a') 
frase1 = frases.find("a") + 1
fraseu = frases.rfind("a") + 1

print(f"{frasec}, {frase1}, {fraseu}")