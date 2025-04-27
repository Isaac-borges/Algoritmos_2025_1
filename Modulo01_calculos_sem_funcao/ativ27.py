# 27. Leia um número inteiro de segundos, calcule e escreva 
# quantas horas, quantos minutos e quantos segundos ele corresponde.

#Entrada
numSegundos = int(input('Insira um numero inteiro de segundos : '))

#Processamento
equivalenteHoras = numSegundos // 3600
sobra = numSegundos % 3600
equivalenteMinutos = sobra // 60
equivalenteSegundos = sobra % 60

#Saida
print(f'Isso equivale à {equivalenteHoras} hora(s) {equivalenteMinutos} minuto(s) e {equivalenteSegundos} segundo(s)')