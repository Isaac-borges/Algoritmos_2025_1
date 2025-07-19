def tiparLetra(letra) :
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        tipo = 'vogal'
    elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        tipo = 'vogal'
    else :
        tipo = 'consoante'

    return tipo

def main() :
    letra = input('letra : ')

    tipo = tiparLetra(letra)

    print(f'A letra é uma {tipo}')

main()