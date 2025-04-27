# 11. Leia um número inteiro (3 dígitos) e escreva o 
# inverso do número. (Ex.: número = 532 ; inverso = 235)

#Entrada
numero = int(input('Numero inteiro 3 digitos: '))

#Processamento
centena = numero // 100
restoCentena = numero % 100
dezena = restoCentena // 10
unidade = restoCentena % 10

inverso = (unidade * 100) + (dezena * 10) + centena

#Saida
print(inverso)