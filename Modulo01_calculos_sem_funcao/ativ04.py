# 4. Leia o valor do dólar e um valor em dólar, 
# calcule e escreva o equivalente em real (R$).

#Entrada
valorDolar = float(input('Valor em dólar : US$ '))

#Processamento
# Considere que a cotação do dólar é 5.85
valorReal = valorDolar * 5.85

#Saida
print(f'O valor US$ {valorDolar:.2f} em reais é R$ {valorReal:.2f}')