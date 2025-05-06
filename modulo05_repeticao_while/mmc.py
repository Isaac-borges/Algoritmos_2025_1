def main():
    num1 = int(input('Num 1 : '))
    num2 = int(input('Num 2 : '))

    resultado = mmc(num1, num2)

    print(f'O MMC é {resultado}')



def mmc(m, n):
    valor = 1

    #while (valor % m != 0) or (valor % n != 0) :
        #Enquanto Valor não for divisivel por M AND Valor não for divisivel por N
        # ^ Iria parar no primeiro que for divisivel por um dos dois
        
    #    valor += 1

    while not (valor % m == 0 and valor % n == 0) :
        valor += 1

    return valor


main()