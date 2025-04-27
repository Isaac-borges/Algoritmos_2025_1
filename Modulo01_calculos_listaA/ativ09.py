# Escreva um programa que aplique um desconto percentual sobre um preço inicial.

#Entrada
precoInicial = int(input('Preço (R$)  : '))
percentDesconto = int(input('Desconto (%): '))

#Processamento
precoFinal = precoInicial - ((precoInicial/100) * percentDesconto)

#Saida
print(f'O preço com desconto é R${precoFinal:.2f}')