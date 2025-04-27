#entrada
salario = float(input('Salario: '))
percentual = float(input('Percentual: '))
#processamento
aumento = (salario / 100) * percentual
novo_salario = salario + aumento

#saida
print('Seu aumento será de R$', aumento)
print('Portanto, seu novo salário será de R$', novo_salario)