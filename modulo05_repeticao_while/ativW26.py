# 26. Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião
# em relação ao filme (1=ótimo, 2=bom, 3=regular, 4=péssimo). Escreva um algoritmo que leia a idade e
# a opinião das pessoas, calcule e mostre ao final: (FLAG: idade = -1).
# · a média das idades das pessoas que responderam ótimo;
# · a quantidade de pessoas que respondeu regular;
# · o percentual de pessoas que respondeu bom entre os entrevistados.

def main() :
    idade = getPositiveInt('Qual sua idade?\n > ')

    while idade 