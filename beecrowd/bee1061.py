def calcularTempo(diaInicio, hrIn, minIn, segIn, diaFinal, hrFim, minFim, segFim) :
    if diaFinal > diaInicio :
        if (hrFim >= hrIn and minFim >= minIn and segFim >= segIn) :
            dias = diaFinal - diaInicio
        else :
            dias = diaFinal - diaInicio - 1
    else : 
        dias = diaInicio - diaFinal

    if diaInicio == diaFinal :
        horas = hrFim - hrIn
    elif diaFinal > diaInicio :
        if (hrFim >= hrIn and minFim >= minIn and segFim >= segIn) :
            horas = hrFim - hrIn
        else :
            horas = 24 - (hrIn - hrFim)

    if minFim < minIn :
        horas -= 1
        minutos = 60 - (minIn - minFim)
    else : 
        minutos = minFim - minIn
    
    if segFim < segIn :
        minutos -= 1
        segundos = 60 - (segIn - segFim)
    else : 
        segundos = segFim - segIn 
    
    print(f'{dias} dia(s)')
    print(f'{horas} hora(s)')
    print(f'{minutos} minuto(s)')
    print(f'{segundos} segundos')

def main() :
    diaInicio = int(input('Dia '))
    hrIn, minIn, segIn = input('').split(' : ')
    hrIn = int(hrIn)
    minIn = int(minIn)
    segIn = int(segIn)
    diaFinal = int(input('Dia '))
    hrFim, minFim, segFim = input('').split(' : ')
    hrFim = int(hrFim)
    minFim = int(minFim)
    segFim = int(segFim)

    calcularTempo(diaInicio, hrIn, minIn, segIn, diaFinal, hrFim, minFim, segFim)

main()