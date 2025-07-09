import string
import unicodedata

def main() :
    pass

def getTextExcept(entrada, caractere_proibido) :
    texto = input(entrada)

    for caractere in texto :
        if caractere == caractere_proibido :
            return getTextExcept(entrada, caractere_proibido)
    
    return texto

def transformarEmNomeArquivo(nome) :
    retirar_caracteres_especiais = str.maketrans('', '', string.punctuation)
    nome_limpo = nome.translate(retirar_caracteres_especiais)
    nome_limpo = retirarAcentos(nome_limpo)

    return nome_limpo + '.txt'

def retirarAcentos(texto) :
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )

def getNomeArquivo(entrada) :
    nome = input(entrada)
    
    nome_arquivo = transformarEmNomeArquivo(nome)

    return nome_arquivo

    





if __name__ == '__main__' :
    main()

