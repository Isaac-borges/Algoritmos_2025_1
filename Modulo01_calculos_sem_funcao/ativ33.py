# 33. Leia um número inteiro (3 dígitos), calcule e 
# escreva a soma do número com seu inverso.
# (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

#Entrada
numero = int(input('Insira um número de 3 dígitos : '))

#Processamento
centena = numero // 100
restoCentena = numero % 100
dezena = restoCentena // 10
unidade = restoCentena % 10

inverso = unidade * 100 + dezena * 10 + centena
soma = numero + inverso

#Saida
print(f'''
A soma desse número com o inverso é
{numero} + {inverso} = {soma}
''')