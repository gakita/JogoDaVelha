import random

def alguem_quase_vencendo(tabuleiro,simbolo):
    for i in range(3):
        #Valida Linhas
        jogada = (0,0)
        count = 0
        count2 = 0
        for j in range(3):
            count2 += 1
            if tabuleiro[i][j] == " ":
                jogada = (i+1,j+1)
            if tabuleiro[i][j] == simbolo:
                count += 1
            if count == 2 and count2 == 3 and jogada != (0,0):
                return jogada

        #Valida Colunas
        jogada = (0, 0)
        count = 0
        count2 = 0
        for j in range(3):
            count2 += 1
            if tabuleiro[j][i] == " ":
                jogada = (j+1,i+1)
            if tabuleiro[j][i] == simbolo:
                count += 1
            if count == 2 and count2 == 3 and jogada != (0,0):
                return jogada

    #Valida Diagonais
    count = 0
    cont2 = 0
    for i in ((0,0),(1,1),(2,2)):
        cont2 += 1
        if tabuleiro[i[0]][i[1]] == " ":
            jogada = (i[0] + 1, i[1] + 1)
        if tabuleiro[i[0]][i[1]] == simbolo:
            count += 1
        if count == 2 and cont2 == 3 and jogada != (0,0):
            return jogada

    count = 0
    cont2 = 0
    for i in ((0, 2), (1, 1), (2, 0)):
        cont2 += 1
        if tabuleiro[i[0]][i[1]] == " ":
            jogada = (i[0] + 1, i[1] + 1)
        if tabuleiro[i[0]][i[1]] == simbolo:
            count += 1
        if count == 2 and cont2 == 3 and jogada != (0,0):
            return jogada

    return (0,0)


def decide_aleatoriamente(tabuleiro,simbolo):
    jogada = (0,0)
    while jogada == (0,0):
        i = random.randint(1,3)
        j = random.randint(1,3)
        if tabuleiro[i-1][j-1] == " ":
            jogada = (i,j)
    return jogada
def decide_jogada(tabuleiro,simbolo):
    if simbolo == "X":
        jogada = alguem_quase_vencendo(tabuleiro,simbolo)
        if jogada != (0,0):
            return jogada
        jogada = alguem_quase_vencendo(tabuleiro,"O")


    if simbolo == "O":
        jogada = alguem_quase_vencendo(tabuleiro,simbolo)
        if jogada != (0,0):
            return jogada
        jogada = alguem_quase_vencendo(tabuleiro,"X")


    if jogada != (0,0):
        return jogada

    return decide_aleatoriamente(tabuleiro,simbolo)