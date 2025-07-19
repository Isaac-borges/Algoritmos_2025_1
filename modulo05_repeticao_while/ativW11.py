# 11. Leia informações de alunos (matrícula, nota1, nota2, nota3) com o fim das informações indicado por
# matrícula = 0. Para cada aluno deve ser calculada a média final de acordo com a seguinte fórmula:

# Média Final = (2 * nota1) + (3 * nota2) + (5 * nota3)
                # ________________________________________
#                                 10

# Se a média final for igual ou superior a 7, o aluno está aprovado; se a média final for inferior a 7, o
# aluno está reprovado. Ao final devem ser mostrados o total de aprovados, o total de reprovados e o total
# de alunos da turma.
from utils_int import getIntMin
from utils_float import getFloatInRange

def getMedia(nota1, nota2, nota3, peso1, peso2, peso3) :
    return ((peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3)) / 10

def main() :
    cont_aprovados = 0
    cont_reprovados = 0 

    matricula_aluno = getIntMin('Matricula aluno : ', 0)
    while matricula_aluno != 0 :
        nota1 = getFloatInRange('Nota 1 : ', 0, 10)
        nota2 = getFloatInRange('Nota 2 : ', 0, 10)
        nota3 = getFloatInRange('Nota 3 : ', 0, 10)
        peso1, peso2, peso3 = 2, 3, 5
        media_final = getMedia(nota1, nota2, nota3, peso1, peso2, peso3)

        if media_final >= 7 :
            print('Aprovado!')
            cont_aprovados += 1
        else : 
            print('Reprovado!')
            cont_reprovados += 1
        
        matricula_aluno = getIntMin('Matricula aluno : ', 0)

    print(f'''
Total alunos     : {cont_aprovados + cont_reprovados} 
Total reprovados : {cont_reprovados}
Total aprovados  : {cont_aprovados}
''')
        
main()