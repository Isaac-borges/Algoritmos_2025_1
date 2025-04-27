# 14. Leia 3 notas de um aluno e o peso de cada nota, 
# calcule e escreva a média ponderada.

#Entrada
nota1 = float(input('Nota 1 : '))
peso1 = float(input('Peso 1 : '))
nota2 = float(input('Nota 2 : '))
peso2 = float(input('Peso 2 : '))
nota3 = float(input('Nota 3 : '))
peso3 = float(input('Peso 3 : '))

#Processamento
mediaPonderada = ((nota1 * peso1)+(nota2 * peso2)+(nota3 * peso3))/(peso1+peso2+peso3)

#Saida
print(f'A média ponderada é {mediaPonderada:.1f}')