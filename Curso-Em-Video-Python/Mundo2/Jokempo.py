import random
import time

opc = ["pedra", "papel", "tesoura"]

x = {
    1: "pedra",
    2: "papel",
    3: "tesoura"
}

print("\033[01;35;40mVamos Jogar Jokempô????\033[0;37;40m")

while True:
    print("\n\033[01;32;40m1\033[03;35;40m - Valores Numéricos\033[0;37;40m")
    print("\033[01;32;40m2\033[03;35;40m - Escrevendo normalmente\033[0;37;40m")
    print("\033[01;31;40m0\033[03;35;40m - Sair\033[0;37;40m")

    esc = input("\033[00;35;40mEscolha 1, 2 ou 0: \033[0;37;40m")

    if esc == "0":
        print("\033[02;31;40mJogo encerrado!\033[00;37;40m")
        break

   
    elif esc == "1":
        while True:
            print("\n\033[01;32;40m1\033[03;35;40m - Pedra\033[0;37;40m")
            print("\033[01;32;40m2\033[03;35;40m - Papel\033[0;37;40m")
            print("\033[01;32;40m3\033[03;35;40m - Tesoura\033[0;37;40m")

            jog = input(
                "\033[00;32;40m1-3\033[00;35;40m | \033[00;32;40m9 Menu\033[00;35;40m | \033[00;31;40m0 Sair: \033[0;37;40m"
            )

            if jog == "0":
                print("\033[02;31;40mJogo encerrado!\033[00;37;40m")
                exit()

            if jog == "9":
                break

            if not jog.isdigit() or int(jog) not in (1, 2, 3):
                print("\033[01;31;40mDigite uma opção válida!!!\033[00;37;40m")
                continue

            jog = int(jog)
            pc = random.choice(opc)

            print(
                f"\033[03;35;40mComputador escolheu: "
                f"\033[01;34;40m{pc} "
                f"\033[00;35;40m| Você escolheu: "
                f"\033[01;34;40m{x[jog]}\033[00;37;40m"
            )

            time.sleep(1)

            if x[jog] == pc:
                print("\033[01;34;40mEmpate!!!\033[00;37;40m")

            elif (
                (jog == 1 and pc == "tesoura") or
                (jog == 2 and pc == "pedra") or
                (jog == 3 and pc == "papel")
            ):
                print("\033[01;32;40mVOCÊ GANHOU!!!!\033[00;37;40m")

            else:
                print("\033[01;31;40mVOCÊ PERDEU!!!\033[00;37;40m")

 
    elif esc == "2":
        while True:
            jog = input(
                "\n\033[00;32;40mPedra\033[00;35;40m, "
                "\033[00;32;40mPapel\033[00;35;40m, "
                "\033[00;32;40mTesoura\033[00;35;40m | "
                "\033[00;32;40mmenu\033[00;35;40m | "
                "\033[00;31;40msair\033[00;37;40m: "
            ).lower()

            if jog == "sair":
                print("\033[02;31;40mJogo encerrado!\033[00;37;40m")
                exit()

            if jog == "menu":
                print("\033[00;35;40mVoltando ao Menu...\033[00;37;40m")
                break

            if jog not in opc:
                print("\033[01;31;40mEscolha uma opção válida!!!\033[00;37;40m")
                continue

            pc = random.choice(opc)

            print(
                f"\033[03;35;40mComputador escolheu: "
                f"\033[01;34;40m{pc} "
                f"\033[00;35;40m| Você escolheu: "
                f"\033[01;34;40m{jog}\033[00;37;40m"
            )

            time.sleep(1)

            if jog == pc:
                print("\033[01;34;40mEmpate!!!\033[00;37;40m")

            elif (
                (jog == "pedra" and pc == "tesoura") or
                (jog == "tesoura" and pc == "papel") or
                (jog == "papel" and pc == "pedra")
            ):
                print("\033[01;32;40mVocê ganhou!!!!\033[00;37;40m")

            else:
                print("\033[01;31;40mVocê perdeu!!!\033[00;37;40m")

    else:
        print("\033[02;31;40mOpção inválida!\033[00;37;40m")
