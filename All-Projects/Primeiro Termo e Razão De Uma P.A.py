print("\033[0;35;40mMe Diga O \033[1;34;40mPrimeiro Termo\033[0;35;40m e a \033[1;34;40mRazão De Uma P.A\033[0;35;40m, Irei Mostrar os 10 Primeiros Termos Dessa Progressão!!!\033[0;37;40m")

p = int(input("\033[0;35;40mMe Diga O Primeiro Termo De Sua P.a:\033[0;37;40m "))
r = int(input("\033[0;35;40mMe Diga A Razão De Sua P.A:\033[0;37;40m "))
for i in range(10):
    print(p)
    p +=r