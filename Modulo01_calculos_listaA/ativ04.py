# Escreva um programa que converta minutos para horas e minutos.

#Entrada
minutosTotal = int(input('Minutos: '))

#Processamento
horasEquiv = minutosTotal // 60
minutosEquiv = minutosTotal % 60

#Saida
print(f'{minutosTotal} minutos equilavem à {horasEquiv} horas e {minutosEquiv} minutos')

