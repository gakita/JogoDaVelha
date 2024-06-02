import random

# Função para verificar se algum jogador está prestes a vencer
def alguem_quase_vencendo(tabuleiro, simbolo):
    for i in range(3):
        # Valida Linhas
        jogada = (0,0)
        count = 0
        count2 = 0
        for j in range(3):
            count2 += 1
            if tabuleiro[i][j] == " ":  # Verifica espaços vazios na linha
                jogada = (i+1,j+1)
            if tabuleiro[i][j] == simbolo:  # Conta quantos símbolos iguais existem na linha
                count += 1
            if count == 2 and count2 == 3 and jogada != (0,0):  # Se houver 2 símbolos iguais e um espaço vazio, retorna a jogada
                return jogada

        # Valida Colunas
        jogada = (0, 0)
        count = 0
        count2 = 0
        for j in range(3):
            count2 += 1
            if tabuleiro[j][i] == " ":  # Verifica espaços vazios na coluna
                jogada = (j+1,i+1)
            if tabuleiro[j][i] == simbolo:  # Conta quantos símbolos iguais existem na coluna
                count += 1
            if count == 2 and count2 == 3 and jogada != (0,0):  # Se houver 2 símbolos iguais e um espaço vazio, retorna a jogada
                return jogada

    # Valida Diagonais
    count = 0
    cont2 = 0
    for i in ((0,0),(1,1),(2,2)):  # Verifica a diagonal principal
        cont2 += 1
        if tabuleiro[i[0]][i[1]] == " ":  # Verifica espaços vazios na diagonal
            jogada = (i[0] + 1, i[1] + 1)
        if tabuleiro[i[0]][i[1]] == simbolo:  # Conta quantos símbolos iguais existem na diagonal
            count += 1
        if count == 2 and cont2 == 3 and jogada != (0,0):  # Se houver 2 símbolos iguais e um espaço vazio, retorna a jogada
            return jogada

    count = 0
    cont2 = 0
    for i in ((0, 2), (1, 1), (2, 0)):  # Verifica a diagonal secundária
        cont2 += 1
        if tabuleiro[i[0]][i[1]] == " ":  # Verifica espaços vazios na diagonal
            jogada = (i[0] + 1, i[1] + 1)
        if tabuleiro[i[0]][i[1]] == simbolo:  # Conta quantos símbolos iguais existem na diagonal
            count += 1
        if count == 2 and cont2 == 3 and jogada != (0,0):  # Se houver 2 símbolos iguais e um espaço vazio, retorna a jogada
            return jogada

    return (0,0)  # Retorna (0,0) se nenhuma jogada estiver prestes a vencer

# Função para decidir uma jogada aleatória
def decide_aleatoriamente(tabuleiro, simbolo):
    jogada = (0,0)
    while jogada == (0,0):
        i = random.randint(1,3)
        j = random.randint(1,3)
        if tabuleiro[i-1][j-1] == " ":  # Verifica se o espaço está vazio antes de escolher a jogada
            jogada = (i,j)
    return jogada

# Função principal para decidir a jogada
def decide_jogada(tabuleiro, simbolo):
    if simbolo == "X":
        jogada = alguem_quase_vencendo(tabuleiro, simbolo)
        if jogada != (0,0):
            return jogada
        jogada = alguem_quase_vencendo(tabuleiro, "O")  # Verifica se o oponente (O) está prestes a vencer

    if simbolo == "O":
        jogada = alguem_quase_vencendo(tabuleiro, simbolo)
        if jogada != (0,0):
            return jogada
        jogada = alguem_quase_vencendo(tabuleiro, "X")  # Verifica se o oponente (X) está prestes a vencer

    if jogada != (0,0):
        return jogada

    return decide_aleatoriamente(tabuleiro, simbolo)  # Se nenhuma jogada iminente de vitória, escolhe aleatoriamente
