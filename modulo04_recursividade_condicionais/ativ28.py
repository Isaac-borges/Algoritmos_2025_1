def modulo(num) :
    if num >= 0 :
        modulo = num 
    else :
        modulo = num * -1
    return modulo
    

def main(): 
    x1, y1 = input('Coordenadas (x1, y1) : ').split(', ')
    x2, y2 = input('Coordenadas (x2, y2) : ').split(', ')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    largura = x1 - x2
    altura = y1 - y2
    largura = modulo(largura)
    altura = modulo(altura)
    area = largura*altura
    
    print(f'A área do retângulo é {area} U.A.')

main()


