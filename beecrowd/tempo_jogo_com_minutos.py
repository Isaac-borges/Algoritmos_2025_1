def calcularTempo(horaInicio, minutoInicio, horaTermino, minutoTermino) :
    terminoHoraTotal = horaTermino
    if horaTermino <= horaInicio :
        if minutoTermino <= minutoInicio : 
            terminoHoraTotal += 24

    if minutoTermino < minutoInicio :
        terminoHoraTotal -= 1
        minutoTermino += 60
    
    minutosDuracao = minutoTermino - minutoInicio
    horasDuracao =  terminoHoraTotal - horaInicio

    print(f'O JOGO DUROU {horasDuracao} HORA(S) E {minutosDuracao} MINUTO(S)')

def main() :
    horaInicio, minutoInicio, horaTermino, minutoTermino = input('').split()
    
    horaInicio = int(horaInicio)
    minutoInicio = int(minutoInicio)
    horaTermino = int(horaTermino)
    minutoTermino = int(minutoTermino)

    calcularTempo(horaInicio, minutoInicio, horaTermino, minutoTermino) 

main()