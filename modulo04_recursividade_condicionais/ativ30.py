from utils_int import getIntInRange

def somar2metades(numero) :
    milhar = numero // 1000
    resto = numero % 1000
    centena = resto // 100
    primeiraMetade = (milhar * 1000) + (centena * 100)
    segundaMetade = numero - primeiraMetade
    primeiraMetade /= 100
    soma = segundaMetade + primeiraMetade
    print(f'{primeiraMetade} + {segundaMetade} = {soma}')

    return soma


def main() :
    numero = getIntInRange('Insira um número de 4 digitos : ', 1000, 9999)

    soma2metades = somar2metades(numero)
    print(f'{soma2metades}² = {numero}')

    if soma2metades**2 == numero :
        print(f'{numero} obedece à regra')
    else : 
        print(f'{numero} não obedece à regra')

main()