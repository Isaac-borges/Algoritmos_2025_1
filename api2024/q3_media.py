import os 

def getIntInRange(entrada, floor, ceiling):
    numero = float(input(entrada))

    if numero % 1 != 0 or numero < floor or numero > ceiling :
        print('Opção inválida!')
        numero = getIntInRange(entrada, floor, ceiling)
    
    return numero

def getNota(entrada, floor, ceiling) :
    nota = float(input(entrada))

    if nota < floor or nota > ceiling :
        print('Nota Inválida!')
        nota = getNota(entrada, floor, ceiling)

    return nota

def menu() :
    print('''
---------------------------------------------------------
          Bem vindo ao sistema de notas!
          Para começar, insira o sexo do aluno:
          0 - Parar
          1 - Mulher
          2 - Homem
---------------------------------------------------------
''')

def maiorORmenor(numero, comparacao, solicitado) :
    if solicitado == 'maior' :
        if numero >= comparacao :
            maior = numero
        else :
            maior = comparacao
        
        return maior
    
    elif solicitado == 'menor' :
        if numero <= comparacao :
            menor = numero
        else :
            menor = comparacao

        return menor

def clearScreen() :
    os.system('cls' if os.name == 'nt' else 'clear')

def getMedia(soma, divisao) :
    return soma / divisao

def enterToContinue() :
    input('ENTER para finalizar')
    
def getDesempenho(media) :
    if media <= 2 :
        desempenho = 'Péssimo'
    elif media <= 4 :
        desempenho = 'Ruim'
    elif media <= 7 : 
        desempenho = 'Regular'
    elif media <= 8 :
        desempenho = 'Bom'
    else :
        desempenho = 'Excelente'

    return desempenho

def main() :
    sexo = None
    qtdMulheres = 0
    qtdHomens = 0
    notaMulheres = 0
    notaHomens = 0
    totalNotaMulheres = 0
    totalNotaHomens = 0
    maiorNotaGeral = -1
    menorNotaGeral = 11

    while sexo != 0 :
        menu()
        sexo = getIntInRange('Sexo do aluno > ', 0, 2)

        if sexo == 1 :
            nota = getNota('Nota da aluna > ', 0, 10)
            qtdMulheres += 1
            maiorNotaGeral = maiorORmenor(nota, maiorNotaGeral, 'maior')
            menorNotaGeral = maiorORmenor(nota, menorNotaGeral, 'menor')
            totalNotaMulheres += nota
        else:
            nota = getNota('Nota do aluno > ', 0, 10)
            qtdHomens += 1
            maiorNotaGeral = maiorORmenor(nota, maiorNotaGeral, 'maior')
            menorNotaGeral = maiorORmenor(nota, menorNotaGeral, 'menor')
            totalNotaHomens += nota
        
        clearScreen()

    numeroAlunos = qtdMulheres + qtdHomens
    if numeroAlunos > 0 :
        totalTurma = totalNotaHomens + totalNotaMulheres
        mediaMulheres = getMedia(totalNotaMulheres, qtdMulheres) if qtdMulheres > 0 else 0
        mediaHomens = getMedia(totalNotaHomens, qtdHomens) if qtdHomens > 0 else 0
        mediaturma = getMedia(totalTurma, numeroAlunos)
        desempenhoTurma = getDesempenho(mediaturma)
        desempenhoM = getDesempenho(mediaMulheres)
        desempenhoH = getDesempenho(mediaHomens)
        print(f'''
    -------------------------------------------
                 RELATORIO DA TURMA
        MAIOR NOTA     : {maiorNotaGeral}
        MENOR NOTA     : {menorNotaGeral}
        MEDIA GERAL    : {mediaturma:.2f}
        MEDIA ALUNOS   : {mediaHomens:.2f}
        PERFORM ALUNOS : {(mediaHomens*10):.2f}%
        MEDIA ALUNAS   : {mediaMulheres:.2f}
        PERFORM ALUNAS : {(mediaMulheres*10):.2f}%
        

        TOTAL TURMA    : {numeroAlunos}
        TOTAL ALUNOS   : {qtdHomens}
        TOTAL ALUNAS   : {qtdMulheres}   


        DESEMPENHO TURMA   : {desempenhoTurma}
        DESEMPENHO ALUNOS  : {desempenhoH}
        DESEMPENHO ALUNAS  : {desempenhoM}
    -------------------------------------------
    ''')
    enterToContinue()
    clearScreen()
    print('FIM')
    

main()