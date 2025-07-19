def main() :
    letra = input('Letra : ')

    if letra == 'F' :
        sexo = 'feminino'
    elif letra == 'M' :
        sexo = 'masculino'
    else :
        sexo = 'inválido'
    
    print(f'O sexo é {sexo}')

main()