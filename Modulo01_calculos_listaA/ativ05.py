#Escreva um programa que determine a quantidade de notas 
#de 50 e 10 necessárias para um determinado valor.

#Entrada
valor = int(input('Valor: '))

#Processamento
numNotas50 = valor // 50
valorRestante = valor - (numNotas50 * 50)
numNotas10 = valorRestante // 10

#Saida
print(f'{numNotas50} nota(s) de 50 e {numNotas10} nota(s) de 10')
