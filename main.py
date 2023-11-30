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
    if depth == 0 or get_game_over(state):
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
    if depth == 0 or get_game_over(state):
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

def get_dogs_position(board):
    dogs_position = {}
    counter_dogs = 0

    for row in range(8):
        for col in range(5):
            if board[row][col] == '1':
                counter_dogs += 1
                dogs_position[counter_dogs] = (row, col)

    return dogs_position

def get_possible_moves_dogs(board):
    possible_moves_dogs = {}
    counter_dogs = 0

    for row in range(8):
        for col in range(5):
            if board[row][col] == '1':
                counter_dogs += 1
                possible_moves_dogs[counter_dogs] = []

                # Verificar frente
                if row + 1 < 8 and board[row + 1][col] == '0':
                    possible_moves_dogs[counter_dogs].append((row + 1, col))

                # Verificar Atrás
                if row - 1 >= 0 and board[row - 1][col] == '0':
                    possible_moves_dogs[counter_dogs].append((row - 1, col))

                # Verificar Esquerda
                if col - 1 >= 0 and board[row][col - 1] == '0':
                    possible_moves_dogs[counter_dogs].append((row, col - 1))

                # Verificar Direita
                if col + 1 < 5 and board[row][col + 1] == '0':
                    possible_moves_dogs[counter_dogs].append((row, col + 1))

                # Verificar Superior Esquerda
                if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == '0':
                    possible_moves_dogs[counter_dogs].append((row - 1, col - 1))

                # Verificar Inferior Esquerda
                if row + 1 < 8 and col - 1 >= 0 and board[row + 1][col - 1] == '0':
                    possible_moves_dogs[counter_dogs].append((row + 1, col - 1))

                # Verificar Superior Direira
                if row - 1 >= 0 and col + 1 < 5 and board[row - 1][col + 1] == '0':
                    possible_moves_dogs[counter_dogs].append((row - 1, col + 1))

                # Verificar Inferior Direira
                if row + 1 < 8 and col + 1 < 5 and board[row + 1][col + 1] == '0':
                    possible_moves_dogs[counter_dogs].append((row + 1, col + 1))

                # Ordenar os movimentos para o cachorro atual
                possible_moves_dogs[counter_dogs] = sorted(possible_moves_dogs[counter_dogs])

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

def is_valid_move_dogs(board, dog, move):
    if move in get_empty_zone(board):
        return False
    
    if board[move[0]][move[1]] != '0':
        return False
    
    if move == get_jaguar_position(board):
        return False
    
    if move[0] < 0 or move[0] >= 8 or move[1] < 0 or move[1] >= 5:
        return False
    
    current_position = get_dogs_position(board)[dog]
    
    valid_moves = [
        (current_position[0] + 1, current_position[1]),
        (current_position[0] - 1, current_position[1]),
        (current_position[0], current_position[1] + 1),
        (current_position[0], current_position[1] - 1),
        (current_position[0] + 1, current_position[1] + 1),
        (current_position[0] - 1, current_position[1] - 1),
        (current_position[0] + 1, current_position[1] - 1),
        (current_position[0] - 1, current_position[1] + 1),
    ]
    
    is_valid = move in valid_moves
    
    return is_valid

def make_move_dogs(board, dog, move):
    if is_valid_move_dogs(board, dog, move):
        current_position = get_dogs_position(board)[dog]

        board[move[0]][move[1]] = '1'
        board[current_position[0]][current_position[1]] = '0'

def is_valid_move_jaguar(board, move):
    if move in get_empty_zone(board):
        return False
    
    if board[move[0]][move[1]] != '0':
        return False

    if move[0] < 0 or move[0] >= 8 or move[1] < 0 or move[1] >= 5:
        return False
    
    current_position = get_jaguar_position(board)
    
    valid_moves = [
        (current_position[0] + 1, current_position[1]),
        (current_position[0] - 1, current_position[1]),
        (current_position[0], current_position[1] + 1),
        (current_position[0], current_position[1] - 1),
        (current_position[0] + 1, current_position[1] + 1),
        (current_position[0] - 1, current_position[1] - 1),
        (current_position[0] + 1, current_position[1] - 1),
        (current_position[0] - 1, current_position[1] + 1),
    ]
    
    is_valid = move in valid_moves
    
    return is_valid

def make_move_jaguar(board, move):
    if is_valid_move_jaguar(board, move):
        current_position = get_jaguar_position(board)

        board[move[0]][move[1]] = '2'
        board[current_position[0]][current_position[1]] = '0'

def get_game_over(board):
    quantity_dogs = 0
    
    for row in range(8):
        for col in range(5):
            if board[row][col] == '1':
                quantity_dogs += 1
    
    if quantity_dogs == 9:            
        return 'Game Over'

def get_game_winner(board):
    if get_jaguar_position(board) in get_prison_zone(board):
        return True
    elif not get_possible_moves_jaguar(board):
        return True
    else:
        return False

def get_prison_zone(board):
    prison_zone_positions = [(5,2), (6,1), (6,2), (6,3), (7,1), (7,2), (7,3)]
    
    return prison_zone_positions

def get_empty_zone(board):
    empty_zone_positions = [(5,0), (5,1), (5,3), (5,4), (6,0), (6,4), (7,0), (7,4)]
    
    return empty_zone_positions

# max_depth = 3
# best_move = alpha_beta_search(tabuleiro, max_depth)
# print("Melhor movimento:", best_move)

print_board(board)
print(f"\nPosição dos Cachorros = {get_dogs_position(board)}\n")
print(f"Movimentos Cachorros = {get_possible_moves_dogs(board)}\n")
print(f"Posição da Onça = {get_jaguar_position(board)}")
print(f"\nMovimentos Onça = {get_possible_moves_jaguar(board)}\n")
print(f"Zona de Prisão = {get_prison_zone(board)}\n")
print(f"Vencedor = {get_game_winner(board)}\n")

# make_move_dogs(board, 14, (3, 4))

# print("\nTabuleiro Após o Movimento:")
# print_board(board)

# make_move_jaguar(board, (5, 2))

# print("\nTabuleiro Após o Movimento:")
# print_board(board)