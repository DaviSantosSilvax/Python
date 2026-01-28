print("\033[35mIrei Fazer Uma Função Que Irá Mostrar o Fatorial De Um Número e Que Se o Parâmetro Show For True, Irá Mostrar Também o Processo!")
print("\033[34m=-"*20)
def fatorial(n=0, show=False):
    """
    ---> Calcula o Fatorial De Um Número.
    :Para n: O Número a Ser Calculado.
    :Para show: (Opcional) Mostrar Ou Não A Conta.
    :Return: O Valor Do Fatorial De Um Número N.
    """
    f = 1
    for i in  range(n, 0, -1):
        if show:
            print(f"\033[32m{i}", end=" \033[33mX " if i > 1 else " \033[33m= \033[35m")
        f *=i
    return f"\033[32m{f}\033[37m"
            

print(fatorial(7, show=True))
print(fatorial(5))