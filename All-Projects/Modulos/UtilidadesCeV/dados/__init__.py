def leiaDinheiro(msg):
    
    while True:
        try:
            v = input(msg).strip().replace(",", ".")
            return float(v)
        except ValueError: 
            print("Valor Inválido")