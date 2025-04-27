# 7. Leia 3 números, calcule e escreva a 
# soma dos 2 primeiros e a diferença entre os 2 últimos.

#Entrada
numero1 = float(input('Insira o primeiro número : '))
numero2 = float(input('Insira o segundo número  : '))
numero3 = float(input('Insira o terceiro número : '))

#Processamento
soma2First = numero1 + numero2
diferenca2Last = numero2 - numero3

#Saida
print(f'''
A soma dos dois primeiros números é    : {soma2First}
A diferença dos dois ultimos números é : {diferenca2Last}
''')