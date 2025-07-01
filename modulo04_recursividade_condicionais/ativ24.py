from utils_float import getFloat

def calculo_bhaskara(a, b, c) :
    delta = b**2 - 4*a*c 
    
    if a == 0 or delta < 0 :
        print('Impossivel calcular')
    else: 
        try :
            R1 = ((b*-1) + delta**0.5) / (2 * a)
            R2 = ((b*-1) - delta**0.5) / (2 * a)
            
            print(f'R1 = {R1:.5f}')
            print(f'R2 = {R2:.5f}')
        except ValueError :
            print('Impossivel calcular')

def main() :
    A = getFloat('')
    B = getFloat('')
    C = getFloat('')
    
    calculo_bhaskara(A, B, C) 

main()