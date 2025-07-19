def ordenarDoisNumeros(x, y) :
    if x > y :
        inicio = y 
        limite = x
    elif y > x : 
        inicio = x
        limite = y
    else :
        inicio = x
        limite = y
    
    return inicio, limite

def main() :
    x = int(input(''))
    y = int(input(''))

    inicio, limite = ordenarDoisNumeros(x, y)
    soma = 0

    for i in range(inicio+1, limite, 1) :

        if i % 2 != 0 :
            soma += i
        
    print(soma)

main()
