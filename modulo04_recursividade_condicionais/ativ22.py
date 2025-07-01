# 22. Leia a hora do início de um jogo e a hora de fim do jogo 
# (cada hora é composta por 2 variáveis inteiras: hora e minuto). 
# Calcule e escreva a duração do jogo (horas e minutos), sabendo-se 
# que o tempo máximo de duração do jogo é de 24 horas e que ele pode 
# iniciar-se em um dia e terminar no dia seguinte.

from utils_int import getIntInRange, getIntMin

def main() :
    horaInicio = getIntInRange('Hora do inicio : ',0, 23)
    minutoInicio = getIntInRange('Minutos :', 0, 59)
    horaFinal = getIntInRange('Hora do inicio : ',0, 23)
    minutoFinal = getIntInRange('Minutos :', 0, 59)
    verificacaoInvalidez = False

    if horaFinal < horaInicio:
        horaFinal += 24
    
    horasDuracao = horaFinal - horaInicio

    if minutoFinal < minutoInicio :
        horasDuracao -= 1
        minutoFinal += 60

        if horaInicio == horaFinal :
            verificacaoInvalidez = True
    
    minutosDuracao = minutoFinal - minutoInicio

    if verificacaoInvalidez == True :
        print('Jogo Inválido') 
    else :
        print(f'O jogo durou {horasDuracao} horas e {minutosDuracao} minutos!')

main()


