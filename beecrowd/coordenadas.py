def main() :
    x, y = input('').split()

    x = float(x)
    y = float(y)

    if x == 0 and y == 0 :
        quadrante = 'Origem' 
    elif x == 0 and y != 0 :
        quadrante = 'Eixo Y'
    elif x != 0 and y == 0 :
        quadrante = 'Eixo X'
    else :
        if x > 0 and y > 0 :
            quadrante = 'Q1'
        elif x < 0 and y > 0 :
            quadrante = 'Q2'
        elif x < 0 and y < 0 :
            quadrante = 'Q3'
        elif x > 0 and y < 0 :
            quadrante = 'Q4'
    
    print(quadrante)

main()