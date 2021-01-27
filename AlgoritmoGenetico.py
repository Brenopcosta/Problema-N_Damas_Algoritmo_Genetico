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
# e o número 8 será em binário 1000