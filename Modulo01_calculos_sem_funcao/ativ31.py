# 31. Leia um número inteiro (4 dígitos binários), 
# calcule e escreva o equivalente na base decimal.

#Entrada
numBinario = int(input('Insira um número binário de 4 dígitos : '))

#Processamento
numBin8 = numBinario // 1000
resta8 = numBinario % 1000
numBin4 = resta8 // 100
resta4 = resta8 % 100
numBin2 = resta4 // 10
numBin1 = resta4 % 10

numDecimal = (numBin8 * 2 ** 3) + (numBin4 * 2 ** 2) + (numBin2 * 2 ** 1) + (numBin1 * 2 ** 0)

#Saida
print(numDecimal)