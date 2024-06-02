import os
import jogador2 as p2  # Importa o módulo jogador2, renomeado como p2

# Função para limpar a tela
# Favor rodar pelo terminal
def clear():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicializa o tabuleiro como uma matriz 3x3 de espaços vazios
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Função para imprimir o tabuleiro
def print_tabuleiro(tabuleiro):
    # Imprime os índices das colunas
    print(" 1 2 3")
    # Limpa a tela antes de imprimir o tabuleiro
    clear()
    # Espaçamento entre as células do tabuleiro
    space = "   "
    # Imprime o cabeçalho das colunas
    print(space, "    1", space, "|", space, "2", space, "|", space, "3")
    # Itera sobre as linhas do tabuleiro
    for i in range(3):
        # Imprime o índice da linha
        print(i+1, "|", space, end=" ")
        # Itera sobre as colunas da linha atual
        for j in range(3):
            # Imprime o valor da célula atual com espaçamento e separadores
            print(tabuleiro[i][j], space, "|", space, end=" ")
        # Quebra de linha após cada linha do tabuleiro
        print()

# Função para registrar uma jogada no tabuleiro
def jogada(tabuleiro, jogada, simbolo):
    # Atualiza a célula correspondente no tabuleiro com o símbolo do jogador
    tabuleiro[jogada[0]-1][jogada[1]-1] = simbolo

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, simbolo):
    # Verifica as linhas e colunas
    for i in range(3):
        # Verifica se todas as células da linha 'i' são iguais ao símbolo
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo:
            return True
        # Verifica se todas as células da coluna 'i' são iguais ao símbolo
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo:
            return True
    # Verifica a diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo:
        return True
    # Verifica a diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo:
        return True
    # Retorna False se não houver vencedor
    return False

# Função para verificar se uma jogada é válida
def jogada_valida(tabuleiro, jogada):
    # Verifica se a jogada está dentro dos limites do tabuleiro
    if jogada[0] < 1 or jogada[0] > 3 or jogada[1] < 1 or jogada[1] > 3:
        return False
    # Verifica se a célula está vazia
    return tabuleiro[jogada[0]-1][jogada[1]-1] == " "

# Função principal do jogo
def game(tabuleiro):
    # Imprime o tabuleiro inicial
    print_tabuleiro(tabuleiro)
    # Loop principal do jogo
    while True:
        # Loop para a jogada do Jogador 1
        while True:
            # Obtém a jogada do Jogador 1
            jogada_feita = (int(input("Jogador 1, escolha a linha: ")), int(input("Jogador 1, escolha a coluna: ")))
            # Verifica se a jogada é válida
            if jogada_valida(tabuleiro, jogada_feita):
                break
        # Registra a jogada do Jogador 1
        jogada(tabuleiro, jogada_feita, "X")
        # Imprime o tabuleiro atualizado
        print_tabuleiro(tabuleiro)
        # Verifica se o Jogador 1 venceu
        if verificar_vencedor(tabuleiro, "X"):
            print("Jogador 1 venceu!")
            break
        # Verifica se há empate (tabuleiro cheio)
        if not any(" " in row for row in tabuleiro):
            print("Empate!")
            break
        # Jogada do Jogador 2 (computador)
        jogada(tabuleiro, p2.decide_jogada(tabuleiro, "O"), "O")
        # Imprime o tabuleiro atualizado
        print_tabuleiro(tabuleiro)
        # Verifica se o Jogador 2 venceu
        if verificar_vencedor(tabuleiro, "O"):
            print("Jogador 2 venceu!")
            break
        # Verifica se há empate (tabuleiro cheio)
        if not any(" " in row for row in tabuleiro):
            print("Empate!")
            break

# Chama a função principal do jogo
game(tabuleiro)
