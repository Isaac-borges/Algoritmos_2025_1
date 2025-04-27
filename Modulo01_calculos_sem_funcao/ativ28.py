# 28. Leia um número inteiro de horas, calcule e escreva quantas
# semanas, quantos dias e quantas horas ele corresponde.

#Entrada
numHoras = int(input('Insira um número inteiro de horas : '))

#Processamento
equivalenteSemanas = numHoras // 168
resta = numHoras % 168
equivalenteDias = resta // 24
equivalenteHoras = resta % 24

#Saida
print(f'Essa quantidade de horas equivale à {equivalenteSemanas} semana(s), {equivalenteDias} dias(s) e {equivalenteHoras} hora(s)')