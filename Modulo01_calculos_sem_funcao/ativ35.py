# 35. Leia um número inteiro (4 dígitos), calcule e escreva a 
# soma dos elementos que o compõem. 
# Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

#Entrada
numero = int(input('Insira um número de 4 dígitos : '))

#Processamento
milhar = numero // 1000
restoMilhar = numero % 1000
centena = restoMilhar // 100
restoCentena = restoMilhar % 100
dezena = restoCentena // 10
unidade = restoCentena % 10

soma = milhar + centena + dezena + unidade

#Saida
print(f'''
A soma dos elementos é : 
{milhar} + {centena} + {dezena} + {unidade} = {soma}
''')