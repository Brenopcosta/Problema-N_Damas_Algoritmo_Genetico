from random import randint
from random import choices

# O tabuleiro será representado por uma lista de tamanho = "número de rainhas". Cada elemento da lista poderá ir de zero há "número de rainhas - 1"
def criaTabuleiro(numeroDeRainhas):
        tabuleiro = []
        for i in range(0, numeroDeRainhas):
            tabuleiro.append(randint(0, numeroDeRainhas - 1))
     
        return tabuleiro

#Codigo para criar um conjunto de tabuleiros
def criaPopulacaoDeTabuleiros(tamanhoPopulacao, numeroDeRainhas):
    populacaoDeTabuleiros = []
    for i in range (0,numeroDeRainhas):
        populacaoDeTabuleiros.append(criaTabuleiro(numeroDeRainhas))
    return populacaoDeTabuleiros

#A representacao na forma binária será passando cada número do tabuleiro para binário
#exemplo, em um tabuleiro 4 X 4 temos:
# [1,3,1,4] => '0001001100010100
#   Para tabalhar com binários, será necessário deixar esplícito o formato deste binário, por exemplo, 
# 1 pode ser representado pelo binário 1, porém, 4 será representado pelo binário 100.
# Para que a mutação mantenha o tamanho do tabuleiro, será necessário padronizar a representação binária de acordo com o número de rainhas no babuleiro.
# Por exemplo, um tabuleiro com tamanho entre 1 a 15 rainhas pode ser representado em um tamanho de 4 caracteres. Ou seja, o número 1 será em binário 0001
# e o número 8 será em binário 1000.


# Dado um número de rainhas, retorna o formato adequado para representar o número em binário
def buscaFormatoRepresentacaoBinaria(numeroDeRainhas):
    if( numeroDeRainhas == 4):
        return '02b'
    if( numeroDeRainhas == 8 ):
        return '03b'
    else:
        return '04b'

# Dado um tabuleiro em lista, retorna o mesmo na forma binária
def conversorParaRepresentacaoBinaria(tabuleiro, formatoBinario):
    tabuleiroEmBinario = ''

    for rainha in tabuleiro:
        tabuleiroEmBinario = tabuleiroEmBinario + format(rainha, formatoBinario)
    return tabuleiroEmBinario

# Dado um tabuleiro em binário, retorna na forma de lista
def conversorParaRepresetacaoDeLista (tabuleiroEmBinario, formatoBinario):
    if(formatoBinario == '02b'):
        tamanhoDoPasso = 2
    if(formatoBinario == '03b'):
        tamanhoDoPasso = 3
        
    tabuleiro = []

    posicaoPonteiroDoConversor = 2

    for i in range(0,len(tabuleiroEmBinario) , tamanhoDoPasso):
        posicaoPonteiroDoConversor = i + tamanhoDoPasso
        tabuleiro.append( int(tabuleiroEmBinario[i:posicaoPonteiroDoConversor] , 2))
    
    return tabuleiro

#-------------------------------------------------------------------------------------- Codigos para avaliação do tabuleiro -------------------------------------------------------------------------
# Como a heurística é baseada em números de ataques. Esta função retorna quantos ataques são possíveis no tabuleiro
def buscarNumeroDeAtaquesNoTabuleiro(tabuleiro):
    numeroDeAtaques = buscarNumeroDeAtaquesNaHorizontal(tabuleiro) + buscarNumeroDeAtaquesNoNordeste(tabuleiro) + buscarNumeroDeAtaquesNoSudeste(tabuleiro) 
    return numeroDeAtaques

# Para cada rainha no tabuleiro, busca quantos ataques são possíveis na horizontal
def buscarNumeroDeAtaquesNaHorizontal(tabuleiro):
    return buscarNumeroDeAtaquesNaDireita(tabuleiro) 

# Para cada rainha no tabuleiro, busca quantos ataques são possíveis
def buscarNumeroDeAtaquesNaDireita(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range (0,len(tabuleiro)):
        for possivelAtaqueNaDireita in range (posicaoRainha,len(tabuleiro)):
            if possivelAtaqueNaDireita == posicaoRainha:
                continue 

            elif tabuleiro[posicaoRainha] == tabuleiro[possivelAtaqueNaDireita]:
                numeroDeAtaques += 1 
                break           
    return numeroDeAtaques

# Analisa o tabuleiro no sentido nordeste de cada rainha, contando o número de ataques possíveis
def buscarNumeroDeAtaquesNoNordeste(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range (0,len(tabuleiro)):
        mapeiaDiagonal = tabuleiro[posicaoRainha]
        for posicaoHorizontal in range (posicaoRainha + 1, len(tabuleiro)):
            mapeiaDiagonal -= 1

            if tabuleiro[posicaoHorizontal] == mapeiaDiagonal:
                numeroDeAtaques += 1
                break
    return numeroDeAtaques

# Analisa o tabuleiro no sentido sudeste de cada rainha, contando o número de ataques possíveis
def buscarNumeroDeAtaquesNoSudeste(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range (0,len(tabuleiro)):
        mapeiaDiagonal = tabuleiro[posicaoRainha]
        for posicaoHorizontal in range (posicaoRainha + 1, len(tabuleiro)):
            mapeiaDiagonal += 1

            if tabuleiro[posicaoHorizontal] == mapeiaDiagonal:
                numeroDeAtaques += 1
                break
    return numeroDeAtaques

#--------------------------------------------------------------------------------- Fim Codigos para avaliação do tabuleiro -------------------------------------------------------------------------

# Função para avalias o tabuleiro no formato binário.
def avaliaTabuleiroEmBinario(tabuleiroEmBinario, formatoBinario):
    return buscarNumeroDeAtaquesNoTabuleiro(conversorParaRepresetacaoDeLista(tabuleiroEmBinario,formatoBinario))

# Função para avaliar uma poupalão de tabuleiros, retorna uma lista com as avaliações do tabuleiro na mesma ordem dos elementos dos tabuleiros e o melhor tabuleiro.
def avaliaPopulacao(tabuleiros):
    avaliacaoDeElementosDaPopulacao = []
    melhorAvaliacao = -1000
    melhorTabuleiro = []

    for tabuleiro in tabuleiros:
        avaliacao =  buscarNumeroDeAtaquesNoTabuleiro(tabuleiro) * (-1) 
        if(avaliacao > melhorAvaliacao):
            melhorAvaliacao = avaliacao
            melhorTabuleiro = tabuleiro
        avaliacaoDeElementosDaPopulacao.append( avaliacao )
    
    return [avaliacaoDeElementosDaPopulacao, melhorTabuleiro, melhorAvaliacao]

# Dada uma populção A de tabuleiros, retorna uma população B baseada na seleção por peso de tabuleiros de A e o melhor tabuleiro. 
# Simulando a fase de seleção do  algoritmo genético
def selecionaElementosNaPopulacaoPorPeso(tabuleiros,tamanhoDaPopulacao , elitismo):
    resultadoAvaliacoes = avaliaPopulacao(tabuleiros)

    listaDeAvaliacoes = resultadoAvaliacoes[0]
    melhorTabuleiro = resultadoAvaliacoes[1]
    melhorAvaliacao = resultadoAvaliacoes[2]

    minimoDaLista = min(listaDeAvaliacoes)

    listaDePesos = []
    if(minimoDaLista == 0):
        return [tabuleiros, melhorTabuleiro, melhorAvaliacao , True]

    if (elitismo == False):
        for avaliacao in listaDeAvaliacoes:
            pesoNormalizado = ((avaliacao - minimoDaLista) / (0 - minimoDaLista)) 
            listaDePesos.append(pesoNormalizado)

        print("Lista de Pesos:")
        print(listaDePesos)
        return [choices(tabuleiros, weights = listaDePesos, k = tamanhoDaPopulacao ), melhorTabuleiro, melhorAvaliacao, False]
    else:
        for avaliacao in listaDeAvaliacoes:
            pesoNormalizado = ((avaliacao - minimoDaLista) / (0 - minimoDaLista)) 
            listaDePesos.append(pesoNormalizado)

        print("Lista de Pesos:")
        print(listaDePesos)
        return [choices(tabuleiros, weights = listaDePesos, k = tamanhoDaPopulacao - 1 ), melhorTabuleiro, melhorAvaliacao, False]


# Função para realizar crossover de dois tabuleiros
def realizaCrossover( tabuleiroA, tabuleiroB ):
    pontoDeCrossover = randint(1, len(tabuleiroA) - 1)
    
    return [tabuleiroA[0:pontoDeCrossover] + tabuleiroB[pontoDeCrossover:] , tabuleiroB[0:pontoDeCrossover] + tabuleiroA[pontoDeCrossover:]]

# Função para realizar mutacao de um tabuleiro
def realizaMutacao( tabuleiro ):
    pontoDeMutacao = randint(0, len(tabuleiro)-1)
    tabuleiro[pontoDeMutacao] = randint(0, len(tabuleiro)-1)
    return tabuleiro

def vaiRealizarCrossover(probabilidadeDeCrossover):
    saida = choices([True,False],[probabilidadeDeCrossover, 1 - probabilidadeDeCrossover ], k = 1)
    return saida[0]

def vaiRealizarMutacao(probabilidadeDeMutacao):
    saida = choices([True,False],[probabilidadeDeMutacao, 1 - probabilidadeDeMutacao ], k = 1)
    return saida[0]


#print(avaliaTabuleiroEmBinario('0001001001000001','02b'))
#conversorParaRepresetacaoDeLista(conversorParaRepresentacaoBinaria([1,2,3,0],'02b'),'02b')
#[[2, 1, 2, 2], [0, 0, 3, 1], [0, 3, 0, 2], [0, 3, 2, 3]]
#print(criaPopulacaoDeTabuleiros(4,4))
#print(avaliaPopulacao([[2, 1, 2, 2], [0, 0, 3, 1], [0, 3, 0, 2], [0, 3, 2, 3]]))
#print(selecionaElementosNaPopulacaoPorPeso([[2, 1, 2, 2], [2, 0, 3, 1], [0, 3, 0, 2], [0, 3, 2, 3]]))

#print(realizaCrossover([2, 1, 2, 2], [2, 0, 3, 1]))
#print(realizaMutacao([1,2,3,4,5,6,7,8,9]))
#print(vaiRealizarCrossover(0.5))


def algoritmoGenetico(tamanhoDaPopulacao, numeroDeRainhas, numeroDeGeracoes, probabilidadeDeCrossover, probabilidadeDeMutacao, elitismo):
    
    populacao = criaPopulacaoDeTabuleiros(tamanhoDaPopulacao,numeroDeRainhas)

    for geracao in range(0,numeroDeGeracoes):
        elementosSelecionados = selecionaElementosNaPopulacaoPorPeso(populacao, tamanhoDaPopulacao, elitismo)
        
        print("Geracao :" + str(geracao) + " Melhor função da geração:" + str(elementosSelecionados[2]))

        if (elementosSelecionados[3] == True):
            print("Solução encontrada")
            break

        populacaoIntermediaria = elementosSelecionados[0]

        if(vaiRealizarCrossover( probabilidadeDeCrossover )):
            populacaoEmCrossover = []

            for i in range (0, len(populacaoIntermediaria), 2):
                if( i + 1 >= len(populacaoIntermediaria)):
                    break
                
                for populacao in realizaCrossover(populacaoIntermediaria[i], populacaoIntermediaria[i+1]):
                    populacaoEmCrossover.append(populacao)

            populacaoIntermediaria = populacaoEmCrossover

        if(vaiRealizarMutacao( probabilidadeDeMutacao )):
            for i in range(0 , len(populacaoIntermediaria)):
                populacaoIntermediaria[i] = realizaMutacao(populacaoIntermediaria[i])
    
        if(elitismo):
            populacaoIntermediaria.append(elementosSelecionados[1])    

        populacao = populacaoIntermediaria
    
    print(populacao)
    return populacao

algoritmoGenetico( 8, 8, 3000, 0.8,0.2, True)

