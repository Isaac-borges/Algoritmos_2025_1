from entradas import getInt


#def getDivisores(num):
#    contador = 1
#    ordemDivisor = 1
#
#    while contador < num  :
#        if num % contador == 0 :
#            print(f'[{ordemDivisor}º] - {contador}')
#            ordemDivisor += 1
#        contador += 1
    
def getDivisores(num):
    contador = 0
    divisores = ''
    while contador < num :
        contador += 1
        if num % contador == 0 :
            if contador == num :
                divisores += f' {contador} '
            else: 
                divisores += f' {contador},'

    
    return divisores


def main() :
    numero = getInt('Insira um número (flag = 0) : ')
    while numero != 0 :
        divisores = getDivisores(numero)
        print(f'Numero : {numero} | Divisores : [{divisores}]')
        numero = getInt('Insira um número (flag = 0) : ')


main()