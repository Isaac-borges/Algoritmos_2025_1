# 16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” 
# se a média das duas notas for maior ou igual a 7,0. Caso a média seja 
# inferior a 7,0, o programa deve ler a nota do exame e calcule a média 
# final. Se esta média for maior ou igual a 5,0, o programa deve escreva 
# “Aprovado”, caso contrário deve escreva “Reprovado”.
from utils_float import getFloatInRange

def main() :
    nota1 = getFloatInRange('Nota 1 : ', 0, 10)
    nota2 = getFloatInRange('Nota 2 : ', 0, 10)

    media = (nota1 + nota2) / 2

    if media >= 7 :
        print('Aprovado!')
    else :
        nota3 = getFloatInRange('Nota de recuperação : ', 0, 10)
        mediaFinal = (nota3 + media) / 2
        if mediaFinal >= 5 : 
            print('Aprovado!')
        else: 
            print('Reprovado!')

main()
    