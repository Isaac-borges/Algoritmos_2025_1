def pedirIntString(entrada, minInt, maxInt) :
    numero, texto = input(entrada).split()
    
    try : 
        numero = int(numero)
    except ValueError :
        return pedirIntString(entrada, minInt, maxInt)

    while numero < minInt or numero > maxInt :
        numero, texto = input(entrada).split()
    
    return numero, texto

def simulacaoCasos(numero_casos) :
    qtdC = 0
    qtdR = 0
    qtdS = 0
    qtdTotal = 0

    for i in range(0, numero_casos, 1) :
        qtd, animal = pedirIntString('', 1, 15)
        if animal == 'R' :
            qtdR += qtd
        elif animal == 'S' :
            qtdS += qtd
        elif animal == 'C' :
            qtdC += qtd
        
        qtdTotal += qtd
        
    relatorio = f'''Total: {qtdTotal} cobaias
Total de coelhos: {qtdC}
Total de ratos: {qtdR}
Total de sapos: {qtdS}
Percentual de coelhos: {(qtdC/qtdTotal)*100:.2f} %
Percentual de ratos: {(qtdR/qtdTotal)*100:.2f} %
Percentual de sapos: {(qtdS/qtdTotal)*100:.2f} %'''
    
    return relatorio

def main() :
    numero_casos = int(input(''))

    relatorio = simulacaoCasos(numero_casos)

    print(relatorio)

main()



