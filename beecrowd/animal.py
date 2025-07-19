def vertebrados() :
    tipo = input('')
    
    if tipo == 'ave' :
        animalPertenceA = aves()
    elif tipo == 'mamifero' :
        animalPertenceA = mamiferos()
    
    return animalPertenceA

def aves() :
    dieta = input('')

    if dieta == 'carnivoro' :
        return 'aguia'
    elif dieta == 'onivoro' :
        return 'pomba'

def mamiferos () :
    dieta = input('')

    if dieta == 'herbivoro' :
        return 'vaca'
    elif dieta == 'onivoro' :
        return 'homem'

def invertebrados() :
    tipo = input('')

    if tipo == 'inseto' :
        animalPertenceA = insetos()
    elif tipo == 'anelideo' :
        animalPertenceA = anelideos()
    
    return animalPertenceA

def anelideos() :
    dieta = input('')

    if dieta == 'hematofago' :
        return 'sanguessuga'
    elif dieta == 'onivoro' :
        return 'minhoca'
    
def insetos() :
    dieta = input('')

    if dieta == 'hematofago' :
        return 'pulga'
    elif dieta == 'herbivoro' :
        return 'lagarta'

def main() :
    subfilo = input('')

    if subfilo == 'vertebrado' :
        animal = vertebrados()
    elif subfilo == 'invertebrado' :
        animal = invertebrados()

    print(animal)

main()