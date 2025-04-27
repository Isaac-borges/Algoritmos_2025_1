# 5. Leia um número inteiro (3 dígitos), calcule e 
# escreva a soma de seus elementos (C + D + U).

#Entrada
numero = int(input('Insira um número inteiro de 3 dígitos : '))

#Processamento
centena = numero // 100
restoCentena = numero % 100
dezena = restoCentena // 10
unidade = restoCentena % 10

soma = centena + dezena + unidade

#Saida
print(f'A soma dos elementos de {numero} ({centena} + {dezena} + {unidade}) é {soma}')