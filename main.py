board = [
    ['1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '1', '2', '1', '1'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['4', '4', '3', '4', '4'],
    ['4', '3', '3', '3', '4'],
    ['4', '3', '3', '3', '4'],
]

def print_board(board):
    for linha in board:
        print(linha)

def alpha_beta_search(state, depth):
    alpha = float('-inf')
    beta = float('inf')
    best_value = float('-inf')
    best_move = None
    possible_moves = get_possible_moves(state)

    for move in possible_moves:
        move_value = min_value(make_move(state, move), depth - 1, alpha, beta)
        if move_value > best_value:
            best_value = move_value
            best_move = move
        alpha = max(alpha, best_value)

    return best_move

def max_value(state, depth, alpha, beta):
    if depth == 0 or game_over(state):
        return evaluate(state)

    value = float('-inf')
    possible_moves = get_possible_moves(state)

    for move in possible_moves:
        value = max(value, min_value(make_move(state, move), depth - 1, alpha, beta))
        if value >= beta:
            return value
        alpha = max(alpha, value)

    return value

def min_value(state, depth, alpha, beta):
    if depth == 0 or game_over(state):
        return evaluate(state)

    value = float('inf')
    possible_moves = get_possible_moves(state)

    for move in possible_moves:
        value = min(value, max_value(make_move(state, move), depth - 1, alpha, beta))
        if value <= alpha:
            return value
        beta = min(beta, value)

    return value

def get_jaguar_position(board):
    for row in range(8):
        for col in range(5):
            if board[row][col] == '2':
               return (row, col)

def get_possible_moves_dogs(board):
    possible_moves_dogs = {}
    counter_dogs = 0

    for row in range(8):
        for col in range(5):
            if board[row][col] == '0':
                counter_dogs += 1
                possible_moves_dogs[counter_dogs] = (row, col)

    return possible_moves_dogs

def get_possible_moves_jaguar(board):
    possible_moves_jaguar = []

    for row in range(8):
        for col in range(5):
            if board[row][col] == '2':
                # Verificar frente
                if board[row + 1][col] == '1' and board[row + 2][col] == '0':
                    possible_moves_jaguar.append((row + 2, col))
                    
                if board[row + 1][col] == '0':
                    possible_moves_jaguar.append((row + 1, col))
                    
                # Verificar Atrás
                if board[row - 1][col] == '1' and board[row - 2][col] == '0':
                    possible_moves_jaguar.append((row - 2, col))
                    
                if board[row - 1][col] == '0':
                    possible_moves_jaguar.append((row - 1, col))
                
                # Verificar Esquerda
                if board[row][col - 1] == '1' and board[row][col - 2] == '0':
                    possible_moves_jaguar.append((row, col - 2))
                    
                if board[row][col - 1] == '0':
                    possible_moves_jaguar.append((row, col - 1))
                
                # Verificar Direita
                if board[row][col + 1] == '1' and board[row][col + 2] == '0':
                    possible_moves_jaguar.append((row, col + 2))
                    
                if board[row][col + 1] == '0':
                    possible_moves_jaguar.append((row, col + 1))
                    
                # Verificar Superior Esquerda
                if board[row - 1][col - 1] == '1' and board[row - 2][col - 2] == '0':
                    possible_moves_jaguar.append((row - 2, col - 2))
                    
                if board[row - 1][col - 1] == '0':
                    possible_moves_jaguar.append((row - 1, col - 1))
                    
                # Verificar Inferior Esquerda
                if board[row + 1][col - 1] == '1' and board[row + 2][col - 2] == '0':
                    possible_moves_jaguar.append((row + 2, col - 2))
                    
                if board[row + 1][col - 1] == '0':
                    possible_moves_jaguar.append((row + 1, col - 1))
                
                # Verificar Superior Direira
                if board[row - 1][col + 1] == '1' and board[row - 2][col + 2] == '0':
                    possible_moves_jaguar.append((row - 2, col + 2))
                    
                if board[row - 1][col + 1] == '0':
                    possible_moves_jaguar.append((row - 1, col + 1))
                    
                # Verificar Inferior Direira
                if board[row + 1][col + 1] == '1' and board[row + 2][col + 2] == '0':
                    possible_moves_jaguar.append((row + 2, col + 2))
                    
                if board[row + 1][col + 1] == '0':
                    possible_moves_jaguar.append((row + 1, col + 1))

    return sorted(possible_moves_jaguar)

# Implemente a lógica para realizar um movimento no estado do jogo
def make_move(board, move):
    pass

# Implemente a lógica para verificar se o jogo acabou no estado atual
def game_over(board):
    pass

# Implemente a lógica para avaliar o estado do jogo
def evaluate(board):
    quantity_dogs = 0
    
    for row in range(8):
        for col in range(5):
            if board[row][col] == '1':
                quantity_dogs += 1
    
    if quantity_dogs == 9:            
        return 'Game Over'

# max_depth = 3
# best_move = alpha_beta_search(tabuleiro, max_depth)
# print("Melhor movimento:", best_move)

print_board(board)
print(f"\nMovimentos Cachorros = {get_possible_moves_dogs(board)}\n")
print(f"Posição da Onça = {get_jaguar_position(board)}")
print(f"\nMovimentos Onça = {get_possible_moves_jaguar(board)}\n")
# print(evaluate(board))