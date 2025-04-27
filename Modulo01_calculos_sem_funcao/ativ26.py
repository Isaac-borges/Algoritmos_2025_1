# 26. Leia um número inteiro de dias, calcule e escreva 
# quantas semanas e quantos dias ele corresponde.

#Entrada
numDias = int(input('Insira um número inteiro de dias : '))

#Processamento
equivalenteSemanas = numDias // 7
equivalenteDias = numDias % 7

#Saida
print(f'Essa quantidade de dias equivale à {equivalenteSemanas} semana(s) e {equivalenteDias} dia(s)')
