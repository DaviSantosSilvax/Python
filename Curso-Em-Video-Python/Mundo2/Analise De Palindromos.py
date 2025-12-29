import time

print("\033[0;35;40mIrei Analisar Sua Frase, Palavra ou Número e Direi Se é Um \033[1;32;40mPALÍNDROMO\033[0;35;40m!!!\033[0;37;40m")
time.sleep(0.8)

while True:
    p = input("\033[0;35;40mDiga Sua Frase, Palavra ou Número Para eu Analisar Se é Um \033[1;32;40mPALÍNDROMO\033[0;35;40m:\033[0;37;40m ")
    
    p_l = p.replace(" ", "").lower()
    i = p_l[::-1]  
    
    time.sleep(0.8)
    print(f"Frase invertida: {i}")
    
    if i == p_l: 
        print("\033[1;32;40mÉ UM PALÍNDROMO!!!\033[0;37;40m")
    else:
        print("\033[1;31;40mNÃO É UM PALÍNDROMO!!!\033[0;37;40m")
