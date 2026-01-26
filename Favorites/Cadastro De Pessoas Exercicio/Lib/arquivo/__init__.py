import os
from Lib.Funções import interface

# pasta ONDE ESTE arquivo.py está
BASE = os.path.dirname(__file__)


def arquivoExiste(nome):
    caminho = os.path.join(BASE, nome)
    return os.path.isfile(caminho)


def criarArquivo(nome):
    caminho = os.path.join(BASE, nome)
    try:
        with open(caminho, "wt+") as a:
            pass
    except Exception as erro:
        print("\033[31mHouve um erro na criação do arquivo:", erro)
    else:
        print(f"\033[32mArquivo \033[34m{nome}\033[32m criado com sucesso!")


def lerArquivo(nome):
    caminho = os.path.join(BASE, nome)
    try:
        with open(caminho, "rt") as a:
            interface.cabeçalho("Pessoas Cadastradas")
            for linha in a:
                dado = linha.split(";")
                dado[1] = dado[1].replace("\n", "")
                print(f"\033[32m{dado[0]:<30}{dado[1]:>3} anos")
    except Exception as erro:
        print("\033[31mErro ao ler o arquivo:", erro)


def cadastrar(nome_arquivo, nome="Desconhecido", idade=0):
    caminho = os.path.join(BASE, nome_arquivo)
    try:
        with open(caminho, "at") as a:
            a.write(f"{nome};{idade}\n")
    except Exception as erro:
        print("\033[31mErro ao escrever no arquivo:", erro)
    else:
        print(f"\033[32mNovo registro de \033[34m{nome}\033[32m adicionado com sucesso!")
