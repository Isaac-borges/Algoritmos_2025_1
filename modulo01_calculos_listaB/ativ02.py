#Entrada
valorFatura = float(input('Valor da fatura : R$ '))

print('------Plano 1------')
pagamentoPlano1 = float(input('Quanto você vai pagar no plano 1 : R$'))
mesesPlano1 = float(input('Quantos meses você vai ficar sem pagar : '))

print('------Plano 2------')
pagamentoPlano2 = float(input('Quanto você vai pagar no plano 2 : R$'))
mesesPlano2 = float(input('Quantos meses você vai ficar sem pagar : '))

#Processamento
#No plano 1: 
devePlano1 = valorFatura - pagamentoPlano1 
valorDividaP1 = devePlano1 * ((1 + 0.15) ** mesesPlano1)

#No plano 2: 
devePlano2 = valorFatura - pagamentoPlano2
valorDividaP2 = devePlano2 * ((1 + 0.15) ** mesesPlano2)

crescimentoPercentual1 = (valorDividaP1 + pagamentoPlano1 - valorFatura) / valorFatura * 100
crescimentoPercentual2 = (valorDividaP2 + pagamentoPlano2 - valorFatura) / valorFatura * 100

#Saida
print(f'''
----------------------------------------------
    Valor inicial da fatura: R$ {valorFatura:.2f}

    No plano 1             :

    Valor pago               : R$ {pagamentoPlano1:.2f}
    Divida final ({mesesPlano1} meses) : R$ {valorDividaP1:.2f}
    Crescimento percentual   : {crescimentoPercentual1:.2f}%

    No plano 2             :

    Valor pago               : R$ {pagamentoPlano2:.2f}
    Divida final ({mesesPlano2} meses) : R$ {valorDividaP2:.2f}
    Crescimento percentual   : {crescimentoPercentual2:.2f}%
----------------------------------------------
''')

