def main() :
    ...

def getText(entrada) :
    texto = input(entrada)

    return texto

def getTextMin(entrada, min) :
    texto = getText(entrada)
    
    while len(texto) < min :
        print(f'Insira um texto com pelo menos {min} caracter(es)!')
        texto = getText(entrada)
    
    return texto

def getTextMax(entrada, max) :
    texto = getText(entrada)

    while len(texto) > max :
        print(f'Insira um texto com até {max} caracter(es)!')
        texto = getText(entrada)
    
    return texto

def has_no_word(palavra: str, letraProibida: str):
    for letra in palavra :
        if letra == letraProibida :
            return False

    return True

def contem_caracter(palavra, caracter) :
    for letra in palavra:
        if letra == caracter:
            return True
    
    return False

def contem_proibidas(palavra, proibidas) :
    for caracter in proibidas :
        if contem_caracter(palavra, caracter):
            return True
    
    return False


def uses_only(palavra, letras_permitidas):
    for caracter in palavra :
        if not contem_caracter(letras_permitidas, caracter) :
            return False
        
    return True

def uses_all(palavra, permitidas):
    for caracter in permitidas :
        if not contem_caracter(palavra, caracter) :
            return False
    
    return True

def is_abecedarian(palavra) :
    anterior = palavra[0]
    for letra in palavra :
        if letra < anterior :
            return False
        anterior = letra
    return True

if __name__ == '__main__' :
    main()