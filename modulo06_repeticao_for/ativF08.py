#8. Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos 
# de N entre os limites lidos.

from utils_int import getInt, getIntMin

def main() :
    numero = getInt('Insira um número : ')
    limiteInferior = getInt('Insira o limite inferior : ')
    limiteSuperior = getIntMin('Insira o limite superior : ', limiteInferior)

    for i in range(limiteInferior, limiteSuperior+1, 1):
        print(f'{numero} x {i} = {numero * i}')
    
main()
