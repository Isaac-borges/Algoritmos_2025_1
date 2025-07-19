# 20. Considere que um carro vai fazer uma viagem entre duas cidades e que a distância a ser percorrida é de
# 600 km. No início da viagem, o carro está com o tanque cheio (50 litros). Durante o percurso foi usado
# um aparelho para medir o desempenho do carro, que mostrava, quando acionado, duas informações:
# · Distância percorrida desde a última medição;
# · Quantidade de litros consumidos para percorrer a distância indicada.
# Escreva um algoritmo que leia estas informações e escreva:
# · se o carro chegou ao seu destino (distância percorrida maior ou igual a 600 km);
# · se o carro parou antes de chegar por falta de combustível (consumo igual a 50 litros);
# · o consumo em km/l do carro.

from utils_float import getFloatInRange, getFloatMin


def main() :
    distancia_percorrida = getFloatMin('Distancia percorrida : ', 0)
    qtd_litros = getFloatInRange('Litros consumidos para percorrer : ', 0, 50)
    litros_restantes = 50 - qtd_litros
    contador = 1

    while distancia_percorrida < 600 and litros_restantes > 0:
        distancia_percorrida += getFloatMin('Distancia percorrida : ', 0)
        qtd_litros += getFloatInRange('Litros consumidos para percorrer : ', 0, litros_restantes)
        litros_restantes -= qtd_litros
        

    chegou_destino = True if distancia_percorrida >= 600 else False
    parou_antes = True if litros_restantes == 0 and chegou_destino == False else False
    media_consumo = distancia_percorrida / qtd_litros
    print(f'''
O carro {'chegou ao destino' if chegou_destino == True else 'não chegou ao destino'}
A gasolina {'foi suficiente' if parou_antes == False else 'não foi suficiente'}
O consumo em km/l do carro é {media_consumo:.2f} km/l
''')
    
main()