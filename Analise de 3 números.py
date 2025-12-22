#SEM LISTA
print("Analiso 3 números e direi eles em ordem crescente")

while True:
    n1 = int(input("Me diga o primeiro número: "))
    n2 = int(input("Me diga o segundo número: "))
    n3 = int(input("Me diga o terceiro número: "))

 
    if n1 <= n2 and n2 <= n3:
        print(n1, n2, n3)
    elif n1 <= n3 and n3 <= n2:
        print(n1, n3, n2)
    elif n2 <= n1 and n1 <= n3:
        print(n2, n1, n3)
    elif n2 <= n3 and n3 <= n1:
        print(n2, n3, n1)
    elif n3 <= n1 and n1 <= n2:
        print(n3, n1, n2)
    else:  
        print(n3, n2, n1)
