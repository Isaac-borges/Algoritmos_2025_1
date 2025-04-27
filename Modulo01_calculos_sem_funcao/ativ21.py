# 21. Leia uma temperatura em °F, calcule e escreva a 
# equivalente em °C. (t°C = (5 * t°F - 160) / 9).

#Entrada
temperaturaF = float(input('Insira a temperatura em °F : '))

#Processamento
temperaturaC = (5 * temperaturaF - 160) / 9

#Saida
print(f'A temperatura em °C é {temperaturaC}')
