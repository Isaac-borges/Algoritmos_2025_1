# 2. Leia um valor em horas e um valor em minutos, 
# calcule e escreva o equivalente em minutos.

#Entrada
valorHoras = int(input('Horas   : '))
valorMinutos = int(input('Minutos : '))

#Processamento
totalMinutos = valorMinutos + (60 * valorHoras)

#Saida

print(f'{valorHoras} e {valorMinutos} minutos equivalem à {totalMinutos} minutos')