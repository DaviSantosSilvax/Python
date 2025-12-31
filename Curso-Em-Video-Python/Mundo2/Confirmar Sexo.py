print("\033[0;35;40mIrei dizer se você é Homem ou Mulher!!!\033[0;34;40m")

s = input("\033[0;35;40mQual seu sexo? [M] ou [F]: \033[0;34;40m").lower()

while s not in ("m", "f"):
    s = input(
        "\033[0;35;40mDigite um sexo válido:\n"
        "[M] Para Masculino\n"
        "[F] Para Feminino\n"
        "\033[0;34;40m"
    ).lower()
if s == "m":
    print("\033[0;32;40mVocê é do sexo Masculino!!!\033[0;37;40m")
else:
    print("\033[0;32;40mVocê é do sexo Feminino!!!\033[0;37;40m")
