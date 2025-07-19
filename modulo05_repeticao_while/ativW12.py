# 12. Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de pingue-pongue, e
# responda quem ganha a partida. A partida chega ao final se:
# · Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2.
# · Se a primeira não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar uma
# diferença de 2 pontos sobre o adversário.
from utils_int import getIntInRange

def main() :
    pont1 = 0
    pont2 = 0
    maiorPont = 0
    menorPont = 0 

    while maiorPont < 21 or maiorPont < menorPont + 2:
        ponto = getIntInRange('Pontuador (1 ou 2) : ', 1, 2)

        if ponto == 1 :
            pont1 += 1
        else :
            pont2 += 1 
        
        print(f'Jogador 1 : {pont1} | Jogador 2 : {pont2}')
        maiorPont = pont1 if pont1 >= pont2 else pont2
        menorPont = pont1 if pont1 <= pont2 else pont2

    print('Vencedor : ' + ('Jogador 1' if pont1 > pont2 else 'Jogador 2'))

main()
    