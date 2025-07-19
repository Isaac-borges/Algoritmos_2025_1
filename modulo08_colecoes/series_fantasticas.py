from utils_visual import clearScreen, enterToContinue
from utils_int import getInt, getIntInRange, getPositiveInt
from utils_float import getFloatInRange
from ulid import ULID
import json

def menu() :
    print('''
-----------------------------------
        SERIES FANTASTICAS
    1 - Adicionar série
    2 - Listar séries
    3 - Listar por ano
    4 - Listar nome e tempo de lançamento
    5 - Listar séries ativas
    6 - Pesquisar parte do nome
    7 - Listar ordenado por ano de lançamento
    8 - Pesquisar por nome de ator e atriz
    9 - ''')

def adicionarSerie() :
    serie = {'id':str(ULID())}
    serie['nome'] = input('Nome da série : ')
    serie['genero'] = input('Gênero : ')
    serie['ano'] = getInt('Ano de lançamento : ')
    serie['temporadas'] = getPositiveInt('Quantidade de temporadas : ')
    serie['avaliacao'] = getFloatInRange('Avaliação [0.0 à 5.0] : ', 0, 5)

    ativa = getIntInRange('A série está ativa? \n (1 - SIM) \n (2 - NÃO) \n > ', 1, 2)
    serie['ativa'] = True if ativa == 1 else False

    return serie

def listarSeries(series) :
    for serie in series :
        print(f'{serie['id']} > Nome: {serie['nome']}; Gênero: {serie['genero']}; Ano: {serie['ano']}; Temporadas: {serie['temporadas']}; Avaliação: {serie['avaliacao']}; Ativa? : {serie['ativa']}')

def filtrarSeries(series, funcao_criterio, criterio) :
    cesta = []

    for serie in series :
        if funcao_criterio(serie, criterio) :
            cesta.append(serie)
    
    return cesta

def filtrarByAno(serie, ano) :
    return serie['ano'] == ano

def main() :
    clearScreen()

    # series = carregarArquivo(arquivo)
    series = []

    opcao = -1 
    while opcao != 0 :
        menu()
        opcao = getIntInRange(' > ', 0, 8)
        clearScreen()
        if opcao == 1 :
            nova_serie = adicionarSerie()
            series.append(nova_serie)
        elif opcao == 2 :
            listarSeries(series)
        elif opcao == 3 :
            ano_filtro = getInt('Qual o ano de lançamento : ')
            clearScreen()
            series_filtradas = filtrarSeries(series, filtrarByAno ,ano_filtro)
            listarSeries(series_filtradas)
        elif opcao == 4 :
            pass 
        
        enterToContinue()
        clearScreen()

main()