#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
#distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor
#seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e
#escreva o custo ao consumidor.

#Entrada
custoFabrica = float(input('Custo de fábrica: '))
percentImposto = float(input('Porcentagem (%) do imposto: '))
percentDistribuidor = float(input('Porcentagem (%) do distribuidor: '))
#Processamento
decimalImposto = percentImposto/100
decimalDistribuidor = percentDistribuidor/100

totalImposto = custoFabrica*decimalImposto
totalDistribuidor = (custoFabrica+totalImposto)*decimalDistribuidor

custoConsumidor = custoFabrica + totalImposto + totalDistribuidor
#Saida
print(f'O custo do carro para o consumidor é R${custoConsumidor:.2f}') #f string