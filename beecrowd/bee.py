def main() :
    contador = 0
    somaNotas = 0
    for i in range(0, 1000, 1) :
        nota = float(input(''))
        if nota < 0 or nota > 10 :
            print('nota invalida')
        else :
            contador += 1
            somaNotas += nota
        
        if contador == 2 :
            break
    
    media = somaNotas / 2
    print(f'media = {media:.2f}')

main()

