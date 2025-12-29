import time
print("\033[0;35;40mIrei Te Mostrar Os Números \033[1;31;40mPARES\033[0;35;40m entre 1 e 50!!!\033[0;37;40m")
input("\033[0;35;40mAperte \033[1;31;40mENTER\033[0;35;40m Para Ver os números \033[0;32;40mPARES\033[0;35;40m Entre \033[1;31;40m1 e 50\033[0;37;40m")
for i in range(2, 51, 2):
    print(i)
    time.sleep(0.5)
print("\033[0;32;40mEstes São os Números \033[1;32;40mPares\033[0;32;40m Entre \033[1;32;40m1 E 50\033[0;32;40m!!!\033[0;37;40m")