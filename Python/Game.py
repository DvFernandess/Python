# Definir a matriz do jogo
board = [' ' for x in range(10)]

# Função para imprimir o tabuleiro
def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# Função para verificar se há espaço livre no tabuleiro
def is_space_free(position):
    return board[position] == ' '

# Função para verificar se o tabuleiro está cheio
def is_board_full(board):
    return board.count(' ') == 1

# Função para adicionar uma jogada no tabuleiro
def make_move(position, symbol):
    board[position] = symbol

# Função para verificar se há um vencedor
def check_winner(board, symbol):
    return (board[1] == board[2] == board[3] == symbol or
            board[4] == board[5] == board[6] == symbol or
            board[7] == board[8] == board[9] == symbol or
            board[1] == board[4] == board[7] == symbol or
            board[2] == board[5] == board[8] == symbol or
            board[3] == board[6] == board[9] == symbol or
            board[1] == board[5] == board[9] == symbol or
            board[3] == board[5] == board[7] == symbol)

# Função para jogar o jogo
def iniciar_jogo():
    print_board(board)

    while not is_board_full(board):
        # Jogada do jogador X
        if check_winner(board, 'X'):
            print('Jogador X venceu!')
            break
        else:
            move = int(input('Jogador X, escolha uma posição (1-9): '))
            if is_space_free(move):
                make_move(move, 'X')
                print_board(board)
            else:
                print('Posição ocupada!')
                continue

        # Jogada do jogador O
        if check_winner(board, 'O'):
            print('Jogador O venceu!')
            break
        else:
            move = int(input('Jogador O, escolha uma posição (1-9): '))
            if is_space_free(move):
                make_move(move, 'O')
                print_board(board)
            else:
                print('Posição ocupada!')
                continue

    if is_board_full(board):
        print('Empate!')

# Iniciar o jogo
iniciar_jogo()