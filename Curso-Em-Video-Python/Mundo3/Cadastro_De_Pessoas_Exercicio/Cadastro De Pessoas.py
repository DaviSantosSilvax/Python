from Lib.Funções import *
from Lib.arquivo import *
from time import sleep

arq = "Arquivocadastro.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = interface.menu(["Visualizar Pessoas", "Cadastrar Pessoa", "Sair Do Sistema"])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        interface.cabeçalho(f"\033[35m{"Novo Cadastro":>38}")
        nome = str(input("\033[35mNome:\033[33m "))
        idade = interface.erro_int("\033[35mIdade:\033[33m ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        sleep(1)
        interface.cabeçalho(f"\033[32m{"Saindo Do Sistema... Até Logo":>37}")
        break
    else:
        print(f"\033[1;31m{"Digite Uma Opção Válida":>37}\033[31m")
    sleep(1.5)
    
