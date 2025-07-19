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
        

def ehMaior(num, comparacao) :
    if num >= comparacao :
        return False
    
    return True

def ehMenor(num, comparacao) :
    if num >= comparacao :
        return False
    
    return True

def main() :

    idades = (12, 43, 14, 13, 64, 123113, 1, -1)
    maior = numMaximoInLista(idades)

    print(maior)

main()