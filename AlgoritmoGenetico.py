# O tabuleiro será representado por uma lista de tamanho = "número de rainhas". Cada elemento da lista poderá ir de zero há "número de rainhas"
def criaTabuleiro(numeroDeRainhas):
        tabuleiro = []
        for i in range(0, numeroDeRainhas):
            tabuleiro.append(randint(1, numeroDeRainhas))
        print("O tabuleiro criado foi:")
        print(tabuleiro)
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
    if(numeroDeRainhas <=8):
        return '04b'
    return '06b'

# Dado um tabuleiro em lista, retorna o mesmo na forma binária
def conversorParaRepresentacaoBinaria(tabuleiro, formatoBinario):
    tabuleiroEmBinario = ''

    for rainha in tabuleiro:
        tabuleiroEmBinario = tabuleiroEmBinario + format(rainha, formatoBinario)
    return tabuleiroEmBinario

# Dado um tabuleiro em binário, retorna na forma de lista
def conversorParaRepresetacaoDeLista (tabuleiroEmBinario, formatoBinario):
    if(formatoBinario == '04b'):
        tamanhoDoPasso = 4
    if(formatoBinario == '06b'):
        tamanhoDoPasso = 6
        
    tabuleiro = []

    posicaoPonteiroDoConversor = 0

    for i in range(4,len(tabuleiroEmBinario) + 1, tamanhoDoPasso):
        tabuleiro.append( int(tabuleiroEmBinario[posicaoPonteiroDoConversor:i] , 2))
        posicaoPonteiroDoConversor = i 
    
    print(tabuleiro)
    return tabuleiro

#-------------------------------------------------------------------------------------- Codigos para avaliação do tabuleiro -------------------------------------------------------------------------
# Como a heurística é baseada em números de ataques. Esta função retorna quantos ataques são possíveis no tabuleiro
def buscarNumeroDeAtaquesNoTabuleiro(tabuleiro):
    numeroDeAtaques = buscarNumeroDeAtaquesNaHorizontal(tabuleiro) + buscarNumeroDeAtaquesNoNordeste(tabuleiro) + buscarNumeroDeAtaquesNoSudeste(tabuleiro) 
    print(numeroDeAtaques)
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


def avaliaTabuleiroEmBinario(tabuleiroEmBinario, formatoBinario):
    return buscarNumeroDeAtaquesNoTabuleiro(conversorParaRepresetacaoDeLista(tabuleiroEmBinario,formatoBinario))



print(avaliaTabuleiroEmBinario('0001001001000001','04b'))
conversorParaRepresetacaoDeLista(conversorParaRepresentacaoBinaria([1,2,3,4,5,6],'04b'),'04b')


