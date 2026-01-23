"""dic = {"Total": len(n), "Maior": max(i), "Menor": min(i), "Média": sum(n)/len(n)}"""

def notas(*nu, sit=False):
    dic = {}
    n = []
    for i in nu:
        n.append(i)

    dic = {"Total": len(n), "Maior": max(n), "Menor": min(n), "Média": sum(n)/len(n)}
    if sit:
        if dic['Média'] >= 7:
            dic["Situação"] = "Boa"
        elif dic['Média'] >= 6:
            dic["Situação"] = "Razoável"
        if dic['Média'] < 6:
            dic["Situação"] = "Ruim"
    return dic
        

resp = notas(10.5, 2, 3.5, sit=True)
print(resp)

