# 20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante 
# (primeiro, segundo, terceiro ou quarto) em que o ângulo se localiza.
from utils_float import getFloatMin

def main() :
    angulo = getFloatMin('Digite o angulo : ', 0)

    if 0 < angulo and angulo < 90 :
        quad = 'primeiro'
    elif 90 < angulo and angulo < 180 :
        quad = 'segundo'
    elif 180 < angulo and angulo < 270 :
        quad = 'terceiro'
    elif 270 < angulo and angulo < 360 :
        quad = 'quarto'
    else : 
        quad = 'no eixo'
    
    print(f'O angulo está no {quad} quadrante' if quad != 'no eixo' else f'O angulo está {quad}')

main()