import math
print("Diga seu angulo e direi seu Seno, cosseno e tangente")
angulo = float(input("Diga quanto vale seu angulo em graus "))

radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"Seu seno vale {seno:.2f} \n seu cosseno vale {cosseno:.2f} \n e sua tangente vale {tangente:.2f}")