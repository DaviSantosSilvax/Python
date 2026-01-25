from Modulos.UtilidadesCeV import moeda
from Modulos.UtilidadesCeV import dados

p = dados.leiaDinheiro("\033[35mDigite Um Preço:\033[33m ")

moeda.resumo(p, 35, 22)