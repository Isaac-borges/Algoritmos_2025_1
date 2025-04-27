# Escreva um programa que receba um número 
# de três dígitos e exiba ele invertido.

#Entrada
numero = int(input('Insira um número de 3 dígitos : '))

#Processamento
centena = numero // 100
centenaResto = numero % 100
dezena = centenaResto // 10
unidade = centenaResto % 10

inverso = (unidade * 100) + (dezena*10) + centena

#Saida
print(f'O inverso desse número é      : {inverso} ')