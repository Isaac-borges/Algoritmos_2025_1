# 32. Leia um número inteiro (3 dígitos), calcule e escreva a 
# diferença entre o número e seu inverso.

#Entrada
numInteiro = int(input('Diga um número inteiro de 3 dígitos: '))

#Processamento
centena = numInteiro // 100
restoCentena = numInteiro % 100
dezena = restoCentena // 10
unidade = restoCentena % 10

inversoInteiro = (unidade * 100) + (dezena * 10) + (centena)
diferenca = numInteiro - inversoInteiro
#Saida
print(f'O inverso de {numInteiro} é {inversoInteiro}')
print(f'E a diferença deles é {diferenca}')