print("\033[35mVou Ler 5 Valores e Guardar Em Uma Lista, ao Final irei Mostrar o Maior e Menor Valor, Também Irei Mostrar em Qual Pergunta Inseriu o Número!!! ")
valores = []
print("\033[36m=-=-"*20)
me = float("inf")
mei = 0
ma = float("-inf")
mai = 0

def leia_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("\033[31mDigite Apenas Números Válidos\033[35m")

valores.append(leia_int("\033[35mPrimeiro Número:\033[33m "))
valores.append(leia_int("\033[35mSegundo Número:\033[33m "))
valores.append(leia_int("\033[35mTerceiro Número:\033[33m "))
valores.append(leia_int("\033[35mQuarto Número:\033[33m "))
valores.append(leia_int("\033[35mQuinto Número:\033[33m "))

for c, i in enumerate(valores):
    if i < me:
        me = i
        mei = c + 1
    if i > ma:
        ma = i
        mai = c + 1
print(f"\033[35mVocê Digitou Os Valores \033[32m{valores}\033[35m!!!")
print(f"\033[35mO Maior Número Foi \033[32m{ma}\033[35m na posição \033[32m{mai}\n\033[35mO Menor Número Foi \033[31m{me}\033[35m na posição \033[31m{mei}\033[37m")