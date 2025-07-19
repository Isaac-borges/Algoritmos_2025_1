from utils_int import getIntMin

def getClube(entrada) :
    clube = input(entrada) 
    while clube != 'a' and clube != 'b' :
        print('Opção inválida!')
        clube = input(entrada)
     
    return clube

def getPontos(classificacao) :
    if classificacao == 1 :
        pontos = 9
    elif classificacao == 2 :
        pontos = 6
    elif classificacao == 3 :
        pontos = 4
    elif classificacao == 4 :
        pontos = 3
    else :
        pontos = 0
    
    return pontos

def main() :
    num_prova, num_nadadores = -1, -1
    pontuacao_a, pontuacao_b = 0, 0

    while num_prova != 0 and num_nadadores != 0 :
        num_prova = getIntMin('Insira o número da prova : ', 0)
        num_nadadores = getIntMin('Insira o número de nadadores : ', 0)
        contador = 0

        while contador < num_nadadores :
            nome = input('Nome do nadador : ')
            classificacao = getIntMin('classificação do nadador : ', 0)
            tempo = getIntMin('Tempo do nadador : ', 0)
            clube = getClube('Clube "a" ou clube "b"? : ')
            pontos = getPontos(classificacao)
            if clube == 'a' :
                pontuacao_a += pontos
            else :
                pontuacao_b += pontos

            contador += 1
        
    print(f'''
Pontuação clube A : {pontuacao_a}
Pontuação clube B : {pontuacao_b}
Vencedor          : {'Clube A' if pontuacao_a > pontuacao_b else 'Clube B' if pontuacao_b > pontuacao_a else 'Empate'}
''')

main()
