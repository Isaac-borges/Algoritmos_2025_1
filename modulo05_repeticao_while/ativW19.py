# 19. Em um frigorífico, cada boi traz em seu pescoço um cartão contendo o seu n.o de identificação e seu
# peso. Escreva um algoritmo que leia um conjunto de cartões e escreva o n.o de identificação e o peso do
# boi mais magro e do boi mais gordo. (Flag: n.o identificação=0)
from utils_int import getIntMin
from utils_float import getFloatMin
def main() :
    n_identificacao = getIntMin('Nº de identificação : ', 0)

    mais_pesado, menos_pesado = 0, 0
    id_mais_pesado, id_menos_pesado = n_identificacao, n_identificacao
    contador = 0
    while n_identificacao != 0 :
        peso_boi = getFloatMin('Peso do boi : ', 0)
        contador += 1

        if contador == 1 :
            mais_pesado, menos_pesado = peso_boi, peso_boi
        else : 
            if peso_boi >= mais_pesado :
                mais_pesado = peso_boi
                id_mais_pesado = n_identificacao
            elif peso_boi <= menos_pesado :
                menos_pesado = peso_boi
                id_menos_pesado = n_identificacao

        n_identificacao = getIntMin('Nº de identificação : ', 0)
    
    print(f'''
MAIS PESADO
Nº de identificação : {id_mais_pesado}
Peso                : {mais_pesado} kg
          
MENOS PESADO 
Nº de identificação : {id_menos_pesado}
Peso                : {menos_pesado} kg

Nº de bois : {contador}
''')

main()