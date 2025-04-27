# 30. Leia um número inteiro de minutos, calcule e escreva quantos 
# dias, quantas horas e quantos minutos ele corresponde.

#Entrada
numMinutos = int(input('Insira um número inteiro de minutos : '))

#Processamento
equivalenteHoras = numMinutos // 60
equivalenteMinutos = numMinutos % 60

#Saida
print(f'Isso equivale à {equivalenteHoras} hora(s) e {equivalenteMinutos} minuto(s)')
