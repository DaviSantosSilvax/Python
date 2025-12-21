import random

print("Um professor quer sortear um dos seus quatro alunos, digite os 4 nomes que irei sortear um deles")
a1 = input("nome do aluno 1 ")
a2 = input("nome do aluno 2 ")
a3 = input("nome do aluno 3 ")
a4 = input("nome do aluno 4 ")
sorteio = random.choice([a1, a2, a3, a4])

print(f"o seu aluno escolhido foi {sorteio}")