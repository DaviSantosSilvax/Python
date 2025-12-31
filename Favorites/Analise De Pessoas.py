print("\033[35mIrei Analisar \033[1;32mNome\033[0;35m,\033[1;32mIdade\033[0;35m e \033[01;32mSexo\033[0;35m de 4 pessoas e Irei dizer:\n"
      "\033[1;34mA Media de Idade do Grupo\n"
      "Qual o Nome do Homem Mais Velho\n"
      "Quantas Mulheres Tem Menos de 20 Anos\033[0;35m")

idadet = 0
idadeh = 0
nf = 0
nomem = ""

for i in range(1, 5):
    print(f"\033[1;32;45m.....:::::\033[1;36;45m{i} Pessoa\033[1;32;45m::::.....\033[0;34;47m")
    nome = input("\033[0;34mNome:\033[0;35m ")
    while not nome.isalpha():
        nome = input("\033[0;34mDigite um nome válido:\033[0;35m ")

    sexo = input("\033[0;34mSexo [M ou F]:\033[0;35m ").strip().lower()
    while sexo not in ("m", "f"):
        sexo = input("\033[0;34mValor inválido, Digite apenas M ou F:\033[0;35m ").strip().lower()

    idade = input("\033[0;34mIdade:\033[0;35m ")
    while not idade.isdigit():
        idade = input("\033[0;34mDigite uma idade válida:\033[0;35m ")
    idade = int(idade)

    idadet += idade

    if sexo == "m" and idade > idadeh:
        idadeh = idade
        nomem = nome
        
    if sexo == "f" and idade < 20:
        nf += 1

media = idadet / 4

print(f"\n\033[0;34mMédia de idade do grupo: \033[0;32m{media:.1f}\033[0;34m")
print(f"\033[0;34mHomem mais velho: \033[0;32m{nomem}\033[0;34m com \033[0;32m{idadeh} anos\033[0;34m")
print(f"Mulheres com menos de 20 anos: \033[0;32m{nf}\033[0;34m")
