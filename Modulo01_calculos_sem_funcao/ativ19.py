# 19. Leia o valor do raio de uma esfera, calcule e escreva seu volume.
# (v = (4 * p * r3) / 3) (p = 3,14)

#Entrada
raio = float(input('Valor do raio (m) : '))

#Processamento
volume = (4 * 3.14 * raio**3) / 3

#Saida
print(f'O volume da esfera é {volume:.2f} m³')