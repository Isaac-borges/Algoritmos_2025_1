# 10. Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a aeronave
# pode levantar vôo ou não. Considere os seguintes critérios:
# · O peso de decolagem da aeronave é sempre igual a 500.000 kg;
# · O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos
# passageiros;
# · O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
# · A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
# · O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
# · O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua
# bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem o peso
# estimado de 10kg.
# O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem
# ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do
# bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume
# de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma
# mensagem indicando a liberação da decolagem ou não.
from utils_int import getPositiveInt, getIntMin
from utils_float import getPositiveFloat
def getPesoBagagem(num_bagagens, valor_anterior) :
    peso_bagagem = 10 
    peso_passageiro = 70

    return valor_anterior + peso_passageiro + (peso_bagagem * num_bagagens)

def getCombustivel(passageiros, carga) :
    peso_aviao_gramas = 500000
    peso_restante = peso_aviao_gramas - (passageiros + carga)

    return peso_restante / 1.5

def main() :
    numero_conteineres = getPositiveInt('Quantos conteineres tem o avião? : ')
    peso_carga = 0
    contador = 0

    while contador < numero_conteineres :
        peso_carga += getPositiveFloat('Qual o peso do conteiner? : ')
        contador += 1
    
    num_bilhete = getIntMin('Numero do bilhete : ', 0)
    peso_passageiros = 0
    num_passageiros = 0
    total_bagagens = 0

    while num_bilhete != 0 :
        qtd_bagagens = getIntMin('Quantidade de bagagem do passageiro : ', 0)
        total_bagagens += qtd_bagagens
        peso_passageiros = getPesoBagagem(qtd_bagagens, peso_passageiros)
        num_passageiros += 1

        num_bilhete = getIntMin('Numero do bilhete : ', 0)

    litros_combustivel = getCombustivel(peso_passageiros, peso_carga)
    pode_voar = 'Sim' if litros_combustivel >= 10000 else 'Não'

    print(f'''
Quantidade de passageiros : {num_passageiros}
Peso de bagagem           : {total_bagagens * 10} kg
Peso de passageiros       : {num_passageiros * 70} kg
Peso de carga             : {peso_carga} kg 
Litros de combustivel     : {litros_combustivel:.1f} L
Pode voar ?               : {pode_voar}
''')

main()


    

