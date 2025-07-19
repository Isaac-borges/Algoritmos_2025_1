from utils_lista import abrirArquivo


def main() :
    escolas = abrirArquivo('enem2014_nota_por_escola.txt')
    niveis = []
    for escola in escolas :
        niveis.append(escola['nivel_socio_economico'])
    
    niveis = set(niveis)

    with open('nivel_socio_economico.txt', 'w') as arquivo:
        for nivel in niveis :
            arquivo.write(f'{nivel}\n')
    
main()
