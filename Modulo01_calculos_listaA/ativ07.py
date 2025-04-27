# Escreva um programa que calcule quantas latas de
#  tinta são necessárias para pintar uma área.

#Entrada
comprimento = int(input('Comprimento: '))
largura = int(input('Largura: '))

#Processamento
latas = comprimento/largura

#Saida
print(f'{latas} Latas de tinta')
