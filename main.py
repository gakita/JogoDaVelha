import os

#Função para limpar a tela
#Favor rodar pelo terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


#Função para imprimir o tabuleiro
def print_tabuleiro(tabuleiro):
    print(" 1 2 3")
    clear()
    space = "   "
    print(space, "    1", space, "|", space, "2", space, "|", space, "3")
    for i in range(3):
        print(i+1, "|", space, end=" ")
        for j in range(3):
            print(tabuleiro[i][j], space, "|", space, end=" ")
        print()

def jogada(tabuleiro, jogada, simbolo):
    tabuleiro[jogada[0]-1][jogada[1]-1] = simbolo

def verificar_vencedor(tabuleiro, simbolo):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo:
        return True
    return False



def game(tabuleiro):
    print_tabuleiro(tabuleiro)
    jogada(tabuleiro, [1, 1], "X")
    print_tabuleiro(tabuleiro)
    jogada(tabuleiro, [1, 2], "O")
    print_tabuleiro(tabuleiro)
    jogada(tabuleiro, [1, 3], "X")
    print_tabuleiro(tabuleiro)
    jogada(tabuleiro, [2, 1], "O")
    print_tabuleiro(tabuleiro)
    jogada(tabuleiro, [2, 2], "X")
    print_tabuleiro(tabuleiro)
    jogada(tabuleiro, [2, 3], "O")
    print_tabuleiro(tabuleiro)
    jogada(tabuleiro, [3, 1], "X")
    print_tabuleiro(tabuleiro)
    jogada(tabuleiro, [3, 2], "O")
    if verificar_vencedor(tabuleiro, "X"):
        print("Vencedor: X")
    elif verificar_vencedor(tabuleiro, "O"):
        print("Vencedor: O")
    else:
        print("Empate")



game(tabuleiro)