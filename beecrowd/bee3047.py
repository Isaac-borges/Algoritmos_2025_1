def getInt(entrada) :
    numero = input(entrada)

    while True :
        try :
            inteiro = int(numero)
            return inteiro
        except ValueError:
            inteiro = input(entrada)

def getIntInRange(entrada, min, max) :
    numero = getInt(entrada)

    while numero < min or max < numero :
        print('Valor Inválido!')
        numero = getInt(entrada)
    
    return numero

def calcularIdade(M, A, B) :
    return (M - A - B)

def numMaximoInLista(lista) :
    for numero in lista :
        if conferirTodosMaior(numero, lista) :
            maior = numero

    return maior

def conferirTodosMaior(num, lista) :
    for i in lista :
        if ehMenor(num, i) :
            return False
        
    return True

def ehMenor(num, comparacao) :
    if num >= comparacao :
        return False
    
    return True

def main() :
    M = getIntInRange('', 40, 110)
    A = getIntInRange('', 1, (M - 1))
    B = getIntInRange('', 1, (M - 1))

    while B == A :
        B = getIntInRange('', 1, (M - 1))
    
    idadeRestante = calcularIdade(M, A, B) 
    idades = (A, B, idadeRestante)
    idadeMaisVelho = numMaximoInLista(idades)

    print(idadeMaisVelho)
    
main()