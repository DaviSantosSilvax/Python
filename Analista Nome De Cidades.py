print('"diga o nome de uma cidade e direi se o primeiro nome dela é "santo" '.title())

cidade = str(input('diga o nome da cidade e direi se ela começa ou não com o nome "Santo" ').title())

if cidade.split()[0] == "Santo":
    print("A Cidade Começa Com 'Santo'!!!! ")
else:
    print("A Cidade Não Começa Com 'Santo'. :()")

