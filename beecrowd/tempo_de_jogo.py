def calcularTempo(inicio, termino) :
    terminoTotal = termino
    if termino <= inicio :
        terminoTotal += 24

    return terminoTotal - inicio

def main() :
    inicio, termino = input('').split()
    
    inicio = int(inicio)
    termino = int(termino)

    duracao = calcularTempo(inicio, termino) 

    print(f'O JOGO DUROU {duracao} HORA(S)')

main()