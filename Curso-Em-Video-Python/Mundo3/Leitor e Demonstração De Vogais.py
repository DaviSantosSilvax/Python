print("\033[35mIrei Mostrar As Vogais Em Varias Palavras Em Uma Tupla!!")
palavras = (
    "computador",
    "programacao",
    "tecnologia",
    "internet",
    "desenvolvimento",
    "algoritmo",
    "python",
    "software",
    "hardware",
    "sistema",
    "dados",
    "rede",
    "seguranca",
    "aplicacao",
    "inteligencia",
    "artificial",
    "banco",
    "informacao",
    "usuario",
    "servidor"
)
vogais = "aeiou"
i = 0
for i in palavras:
     print(f"\n\033[03;36mNa Palavra {i}, Temos as Vogais:\033[1;34m", end="")
     for letra in i:
          if letra in "aeiou":
               print(letra.upper(), end=" ")


    
