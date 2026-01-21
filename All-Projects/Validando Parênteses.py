print("\033[35mDigite Uma Expressão Com Parênteses e Direi Se Ela é Válida!!")
l = []

n = input("\033[35mDigite Sua Expressão: \033[33m")

for i in n:
    if i == "(":
        l.append("(")
    elif i == ")":
        if 0 < len(l):
            l.pop()
        else:
            l.append(")")
            break


if len(l) == 0:
    print("\033[32mSua Expressão Está Válida!!!")
else:
    print("\033[31mSua Expressão Está inválida!!!\033[37m")