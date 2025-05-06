# Exercício 4: Sistema de Notas Escolares
from entradas import getNumberInRange

def calcularMedia(n1, n2, n3):
    media = (n1 + n2 + n3) / 3

    return media

def situacaoAluno(n1, n2, n3, media): 
    situacao = ... 
    
    if n1 == 0 or n2 == 0 or n3 == 0 :
        situacao = 'REPROVADO POR ZERAR'
        return situacao
    
    if media >= 7 :
        situacao = 'APROVADO'
    elif media >= 5 :
        situacao = 'DE RECUPERAÇÃO'
    else :
        situacao = 'REPROVADO'

    return situacao


def main():
    nota1 = getNumberInRange('Nota 1 : ', 0, 10)
    nota2 = getNumberInRange('Nota 2 : ', 0, 10)
    nota3 = getNumberInRange('Nota 3 : ', 0, 10)

    media = calcularMedia(nota1, nota2, nota3)
    situacao = situacaoAluno(nota1, nota2, nota3, media)

    print(f'''
    A média do aluno é : {media:.1f}
    E ele está {situacao}!
''')


main()