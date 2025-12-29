print("\033[0;35;40mDigite \033[1;32;40m6 Números\033[0;35;40m!! Irei Mostrar a Soma Daqueles Que Forem Par, \033[0;31;40mOs que Forem Impar Irei Desconsiderar\033[0;35;40m!!\033[0;37;40m")
soma = 0
for i in range(1, 7):
    n = int(input("Digite O Número Inteiro!!!"))
    if n % 2 == 0:
       soma += n
  
print(f"\033[0;35;40mA Soma Dos Números Considerando Apenas Os Pares É \033[0;32;40m{soma}\033[0;35;40m!!!\033[0;37;40m")

