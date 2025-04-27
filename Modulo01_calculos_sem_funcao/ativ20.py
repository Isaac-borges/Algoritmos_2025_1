# 20. Leia uma temperatura em °C, calcule e escreva a 
# equivalente em °F. (t°F = (9 * t°C + 160) / 5)

#Entrada
temperaturaC = float(input('Temperatura em °C : '))

#Processamento
temperaturaF = (9 * temperaturaC + 160) / 5

#Saida
print(f'A temperatura em °F é {temperaturaF:.1f}')