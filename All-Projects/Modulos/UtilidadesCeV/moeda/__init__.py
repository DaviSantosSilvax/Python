def metade(n, t=False):
    if t == True:
        n = n / 2
        return f"R$ {n:.2f}".replace(".", ",")
    else:
        return n / 2


def dobro(n, t=False):
    if t == True:
        n = n*2
        return f"R$ {n:.2f}".replace(".", ",")
    else:
        return n*2


def aumentar(n, p, t=False):
    if t == True:
        n = n + (n*(p/100))
        return f"R$ {n:.2f}".replace(".", ",")
    else:
        return n + (n*(p/100))


def diminuir(n, p, t=False):
    if t == True:
        n = n - (n*(p/100))
        return f"R$ {n:.2f}".replace(".", ",")
    else:
        return n - (n*(p/100))


def moeda(n):

    return f"R$ {n:.2f}".replace(".", ",")



def resumo(n, a, d):
    print("\033[34m-"*20)
    print("\033[35m  Resumo Do Valor")
    print("\033[34m-"*20)
    print(f"\033[35mPreço Analisado: \033[32mR${n:.2f}".replace(".", ","))
    print(f"\033[35mDobro Do Preço: \033[32m{dobro(n, True)}")
    print(f"\033[35mMetade Do Preço: \033[32m{metade(n, True)}")
    print(f"\033[35m{a}% De Aumento: \033[32m{aumentar(n, a, True)}")
    print(f"\033[35m{d}% De Redução: \033[32m{diminuir(n, d, True)}\033[37m")















"""def metade(n, t):
    return n / 2


def dobro(n, t):
    return n*2


def aumentar(n, p, t):
    return n + (n*(p/100))


def diminuir(n, p, t):
    return n - (n*(p/100))


def moeda(n):

    return f"R$ {n:.2f}".replace(".", ",")"""
