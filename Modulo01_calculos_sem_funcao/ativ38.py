# 38. Leia 2 (duas) frações (numerador e denominador), calcule e escreva 
# a soma destas frações, escrevendo o resultado em forma de fração.

#Entrada
numerador1 = int(input('1º numerador : '))
denominador1 = int(input('1º denominador : '))
numerador2 = int(input('2º numerador : '))
denominador2 = int(input('2º denominador : '))

#Processamento
novoNumerador = (numerador1 * denominador2) + (numerador2 * denominador1)
novoDenominador = denominador1 * denominador2

#Saida
print(f'O resultado será {novoNumerador}/{novoDenominador}')

