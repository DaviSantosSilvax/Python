from datetime import date
print("\033[35mIrei Ler Seus Dados, colocalos em uma lista e mostrá-los")

hoje = date.today()
ano = hoje.year
opc = ["s", "n"]
def valores_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("\033[31mErro, Digite Valor Válido!!\033[35m")
        
def flot(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("\033[31mErro, Digite Valor Válido!!\033[35m")


nome = str(input("\033[35mQual Seu Nome?\033[33m "))
while not nome.replace(" ", "").isalpha():
    nome = str(input("\033[35mQual Seu Nome?\033[33m "))
anon = valores_int("\033[35mQual Seu Ano De Nascimento?\033[33m ")
while anon > hoje.year:
    anon = valores_int("\033[35mQual Seu Ano De Nascimento?(Digite Um Válido)\033[33m ")
idade = ano - anon
print(idade)

ct = str(input("\033[35mVocê Tem Carteira De Trabalho [S] ou [N]:\033[33m ")).lower()
if ct not in opc:
    while ct not in opc:
            ct = str(input("\033[35mVocê Tem Carteira De Trabalho [S] ou [N]:\033[33m ")).lower()
    
if ct == "n":
    rg = {"nome": nome, "idade": idade,"Carteira De Trabalho": "Não"}
    print(rg)
elif  ct == "s":
    contrato = valores_int("\033[35mQuantos Anos De Contratação Na Carteira?\033[33m ")
    sal = flot("\033[35mQual Seu Salário?\033[33m ")
    apos = ( 35 - contrato) + idade
    if contrato >= 35:
        rg = {"nome": nome, "idade": idade,"Carteira De Trabalho": "Sim", "Contratação": contrato, "Salário": sal, "Aposentadoria": "Já Permitida"}
    else:  
        rg = {"nome": nome, "idade": idade,"Carteira De Trabalho": "Sim", "Contratação": contrato, "Salário": sal, "Aposentadoria": apos}
    for k, i in rg.items():
        print(f"{k}: {i}")