from utils_int import getIntInRange

def ehQuadradoPerfeito(numero) :
    milhar = numero // 1000
    resto = numero % 1000
    centena = resto // 100
    primeiraMetade = (milhar * 1000) + (centena * 100)
    segundaMetade = numero - primeiraMetade
    primeiraMetade /= 100
    print(f'{primeiraMetade} + {segundaMetade} = {primeiraMetade + segundaMetade}')
    raiz = numero**0.5
    print(f'A raiz de {numero} é {raiz}')

    if raiz == (primeiraMetade + segundaMetade) :
        return 'é quadrado perfeito'
    else : 
        return 'não é quadrado perfeito'
    
    


def main() :
    numero = getIntInRange('Insira um número de 4 digitos : ', 1000, 9999)

    quadradoPerfeito = ehQuadradoPerfeito(numero)

    print(f'O número {quadradoPerfeito}')

main()