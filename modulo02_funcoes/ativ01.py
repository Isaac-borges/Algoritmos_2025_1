# Leia uma velocidade em m/s, calcule e
# escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

def conversaoMS_KMH(velMS: float):
    velKMH = velMS * 3.6

    return velKMH

def main():
    #Entrada
    velocidadeMS = int(input('Velocidade (m/s): '))

    #Processamento
    velocidadeKMH = conversaoMS_KMH(velocidadeMS)

    #Saida
    print(f'A velocidade em km/h é : {velocidadeKMH}')


main()