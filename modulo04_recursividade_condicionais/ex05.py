# Exercício 5: Calculadora de Descontos
from entradas import getFloat, getNumberInRange

def descontoBase(preco) :
    desconto = 0

    if preco > 500 :
        desconto = 0.15
    elif preco >= 200 :
        desconto = 0.10
    elif preco >= 100 :
        desconto = 0.05

    return desconto

def descontoAdd(vip, aniv) :
    descontoVip = 0 
    descontoAniv = 0

    if vip == 1 :
        descontoVip = 0.05
    
    if aniv == 1 : 
        descontoAniv = 0.03

    descontoTotal = descontoAniv + descontoVip

    return descontoTotal

def calcularDesconto(preco, base, add):
    desconto = base + add

    precoNovo = preco - (preco*desconto)

    return precoNovo

def main(): 
    preco = getFloat('Valor total da compra : R$')
    print('(Sim -> 1)')
    print('(Não -> 0)')
    clienteVip = getNumberInRange('Cliente VIP?    : ', 0, 1)
    clienteAniversario = getNumberInRange('Aniversariante? : ', 0, 1)

    #DESCONTOS
    descontobase = descontoBase(preco)
    descontoadd = descontoAdd(clienteVip, clienteAniversario)
    precoDescontado = calcularDesconto(preco, descontobase, descontoadd)

    #EXIBICAO NA NOTA
    descontoTexto = f'{descontobase * 100}%'
    textoVIP = '0%'
    if clienteVip == 1 :
        textoVIP = '5%'

    textoAniv = '0%'
    if clienteAniversario == 1 :
        textoAniv = '3%'

    print(f'''
---------------------------------------------------------
          OBRIGADO POR COMPRAR EM NOSSA LOJA
    VALOR ORIGINAL : R$ {preco:.2f}
    DESCONTO BASE  : {descontoTexto}
    CLIENTE VIP    : {textoVIP} 
    ANIVERSARIANTE : {textoAniv}
    DESCONTO TOTAL : {(descontobase + descontoadd) * 100}%

    VALOR FINAL    : R${precoDescontado:.2f}
    
---------------------------------------------------------
''')
    

main()


