print("\033[35mIrei Fazer Uma Mensagem Para Você Que Acompanha As Linhas!!")
def mensagem(txt):
    conta = len(txt)
    print(f"\033[34m{'~'*(conta+2)}")
    print(f"\033[32m{txt}")
    print(f"\033[34m{'~'*(conta+2)}")

teste = str(input("Escreva Alguma Coisa:\033[33m "))

mensagem(f" {teste}")