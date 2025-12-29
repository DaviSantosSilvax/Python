print("\033[0;35;40m Irei Dizer Se Seu Número é \033[1;32;40mPrimo\033[0;35;40m ou \033[1;31;40mNão\033[0;35;40m!!\033[0;37;40m")


s = 0
n = int(input("\033[0;35;40m Me Diga Um Número Inteiro Para Análise:\033[0;37;40m  "))
for i in range(1, n+1):
    if n % i == 0:
         print(f"\033[0;31;40m", end=" ")
         s += 1
    else:
         print(f"\033[0;35;40m", end=" ")
    print(f"{i}", end=" ")
if s == 2:
     print(f"\n\033[35;40mO Número \033[01;32m{n}\033[35;40m é \033[01;32mÉ PRIMO!!!\033[0;35;40m Ele é Divisivel Apenas Por 1 e Ele Mesmo!!!\033[37;40m ")
else:
      print(f"\n\033[1;35;40mO número \033[31;40m{n} não é primo\033[0;35;40m, ele foi divisivel \033[01;31;40m{s-2}\033[35;40m Vezes Além de 1 e por Ele Mesmo!!!")

      

            
            
            



   