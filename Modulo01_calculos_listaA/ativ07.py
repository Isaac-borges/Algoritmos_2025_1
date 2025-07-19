# Escreva um programa que calcule quantas latas de
#  tinta são necessárias para pintar uma área.

#Entrada
comprimento = int(input('Comprimento: '))
altura = int(input('Largura: '))

#Processamento
latas = comprimento/altura

#Saida
print(f'{latas} Latas de tinta')
