# 15. Leia um número (entre 0 e 255) na base decimal, calcule e escreva este número na base binária
# e na base hexadecimal.
from utils_int import getIntInRange

def toBinario(num) :
    sucessivo = num
    binario = ''
    while sucessivo >= 1 :
        resto = sucessivo % 2
        sucessivo = sucessivo // 2
        
        binario = str(resto) + binario
    
    return binario

def toHex(num) :
    sucessivo = num
    hexadecimal = ''
    while sucessivo >= 1 :
        resto = sucessivo % 16
        sucessivo = sucessivo // 16
        
        if resto >= 10 :
            caractere = hexLetra(resto)
        else :
            caractere = str(resto)
        
        hexadecimal = caractere + hexadecimal
    
    return hexadecimal 

def hexLetra(resto) :
    if resto == 10 :
        letra = 'A'
    elif resto == 11 :
        letra = 'B'
    elif resto == 12 :
        letra = 'C'
    elif resto == 13 :
        letra = 'D' 
    elif resto == 14 :
        letra = 'E'
    elif resto == 15 :
        letra = 'F'

    return letra

def main() :
    numero = getIntInRange('Numero : ', 0, 255)
    binario = toBinario(numero)
    hexadecimal = toHex(numero)

    print(binario if numero > 0 else 0)
    print(hexadecimal if numero > 0 else 0)

main()