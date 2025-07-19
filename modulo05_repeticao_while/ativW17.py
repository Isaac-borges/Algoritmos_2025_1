# 17. Em um concurso de beleza, cada candidata tem um cartão contendo nome, altura e peso. Escreva um
# algoritmo que leia um conjunto de cartões e escreva o nome e a altura da candidata mais alta e da mais
# baixa; o nome e o peso da candidata mais magra e da mais gorda. (Flag: nome = 'FIM').

from utils_float import getPositiveFloat

def main() :  
    mais_alta, menos_alta = '', ''
    altura_mais_alta, altura_menos_alta = 0, 0 
    mais_gorda, menos_gorda = '', ''
    peso_mais_gorda, peso_menos_gorda = 0, 0

    contador = 0
    nome = input('Nome (flag \'FIM\'): ')
    while nome != 'FIM' :
        contador += 1
        peso = getPositiveFloat('Peso (kg) :')
        altura = getPositiveFloat('Altura (cm) : ')
    
        if contador == 1 :
            mais_alta, menos_alta = nome, nome
            altura_mais_alta, altura_menos_alta = altura, altura
            mais_gorda, menos_gorda = nome, nome
            peso_mais_gorda, peso_menos_gorda = peso, peso
        else :
            if altura >= altura_mais_alta :
                mais_alta = nome
                altura_mais_alta = altura
            elif altura <= altura_menos_alta :
                menos_alta = nome
                altura_menos_alta = altura
            
            if peso >= peso_mais_gorda :
                mais_gorda = nome
                peso_mais_gorda = peso
            elif peso <= peso_menos_gorda :
                menos_gorda = nome
                peso_menos_gorda = peso
        
        nome = input('Nome (flag \'FIM\'): ')  
    
    print(f'''
RELATORIO
Candidata mais alta:
- Nome: {mais_alta}
- Altura: {altura_mais_alta:.2f} m

Candidata mais baixa:
- Nome: {menos_alta}
- Altura: {altura_menos_alta:.2f} m

Candidata mais magra:
- Nome: {menos_gorda}
- Peso: {peso_menos_gorda:.2f} kg

Candidata mais gorda:
- Nome: {mais_gorda}
- Peso: {peso_mais_gorda:.2f} kg
''')

main()





