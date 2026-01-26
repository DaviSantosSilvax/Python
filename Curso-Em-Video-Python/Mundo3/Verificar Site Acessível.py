
import requests
print("\033[35mIrei Mostrar Se o Site Do Pudim\033[33m(https://pudim.com.br/)\033[35m Está Acessível No Momento!!!")
def verificação(url):
    try:
        requests.get(url)
    except:
        print("\033[31mO Site Do Pudim Não Está Acessível No Momento.")
    else:
        print("\033[32mO Site Do Pudim Está Acessível!!!")

verificação("https://pudim.com.br/")
