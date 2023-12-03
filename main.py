# Equipe
# Kauan Deyvid Bezerra de Sousa - 510270
# Marcos Gabriel De Mesquita Mauricio - 509127
# Billy Grahan Alves Rodrigues - 508010

board = [
    ['1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '0', '1'],
    ['2', '1', '0', '1', '0'],
    ['0', '0', '0', '0', '0'],
    ['4', '4', '3', '4', '4'],
    ['4', '3', '3', '3', '4'],
    ['4', '3', '3', '3', '4'],
]

def print_board(board):
    print("Tabuleiro Atual".center(25))
    for linha in board:
        print(linha)

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
    if get_possible_moves_jaguar_eat_dog(board):
        return (get_possible_moves_jaguar_eat_dog(board), 1)
    else:
        return (get_possible_moves_jaguar_empty_space(board), 0)

def get_possible_moves_jaguar_eat_dog(board):
    possible_moves_jaguar = []

    for row in range(8):
        for col in range(5):
            if board[row][col] == '2':
                # Verificar movimentos na vertical
                if row + 2 < 8 and board[row + 1][col] == '1' and board[row + 2][col] == '0':
                    possible_moves_jaguar.append((row + 2, col))
                    
                if row - 2 >= 0 and board[row - 1][col] == '1' and board[row - 2][col] == '0':
                    possible_moves_jaguar.append((row - 2, col))
                    
                # Verificar movimentos na horizontal
                if col + 2 < 5 and board[row][col + 1] == '1' and board[row][col + 2] == '0':
                    possible_moves_jaguar.append((row, col + 2))
                    
                if col - 2 >= 0 and board[row][col - 1] == '1' and board[row][col - 2] == '0':
                    possible_moves_jaguar.append((row, col - 2))
                
                # Verificar movimentos na diagonal
                if row - 2 >= 0 and col - 2 >= 0 and board[row - 1][col - 1] == '1' and board[row - 2][col - 2] == '0':
                    possible_moves_jaguar.append((row - 2, col - 2))
                    
                if row + 2 < 8 and col - 2 >= 0 and board[row + 1][col - 1] == '1' and board[row + 2][col - 2] == '0':
                    possible_moves_jaguar.append((row + 2, col - 2))
                    
                if row - 2 >= 0 and col + 2 < 5 and board[row - 1][col + 1] == '1' and board[row - 2][col + 2] == '0':
                    possible_moves_jaguar.append((row - 2, col + 2))
                    
                if row + 2 < 8 and col + 2 < 5 and board[row + 1][col + 1] == '1' and board[row + 2][col + 2] == '0':
                    possible_moves_jaguar.append((row + 2, col + 2))
                    
    return sorted(possible_moves_jaguar)

def get_possible_moves_jaguar_empty_space(board):
    possible_moves_jaguar = []

    for row in range(8):
        for col in range(5):
            if board[row][col] == '2':
                # Verificar movimentos na vertical
                if row + 1 < 8 and board[row + 1][col] == '0':
                    possible_moves_jaguar.append((row + 1, col))
                    
                if row - 1 >= 0 and board[row - 1][col] == '0':
                    possible_moves_jaguar.append((row - 1, col))
                
                # Verificar movimentos na horizontal
                if col + 1 < 5 and board[row][col + 1] == '0':
                    possible_moves_jaguar.append((row, col + 1))

                if col - 1 >= 0 and board[row][col - 1] == '0':
                    possible_moves_jaguar.append((row, col - 1))
                
                # Verificar movimentos na diagonal
                if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == '0':
                    possible_moves_jaguar.append((row - 1, col - 1))
                    
                if row + 1 < 8 and col - 1 >= 0 and board[row + 1][col - 1] == '0':
                    possible_moves_jaguar.append((row + 1, col - 1))
                    
                if row - 1 >= 0 and col + 1 < 5 and board[row - 1][col + 1] == '0':
                    possible_moves_jaguar.append((row - 1, col + 1))
 
                if row + 1 < 8 and col + 1 < 5 and board[row + 1][col + 1] == '0':
                    possible_moves_jaguar.append((row + 1, col + 1))

    return sorted(possible_moves_jaguar)

def get_position_board(position):
    value_board = 0
    
    for row in range(8):
        for col in range(5):
            if row == position[0] and col == position[1]:
                return value_board
            
            value_board += 1

def is_valid_move_dogs(board, dog, move):
    for position in get_possible_moves_dogs(board)[dog]:
        if position == move:
            return True
    
    return False

def make_move_dogs(board, dog, move):
    if is_valid_move_dogs(board, dog, move):
        current_position = get_dogs_position(board)[dog]

        board[move[0]][move[1]] = '1'
        board[current_position[0]][current_position[1]] = '0'

def is_valid_move_jaguar(board, move):
    check_moves = get_possible_moves_jaguar(board)
    
    for position in check_moves[0]:
        if position == move:
            return (True, check_moves[1])
    
    return False

def make_move_jaguar(board, move):
    check_moves = is_valid_move_jaguar(board, move)

    if check_moves[0]:
        current_position = get_jaguar_position(board)

        if check_moves[1] == 0:
            board[move[0]][move[1]] = '2'
            board[current_position[0]][current_position[1]] = '0'
        else:
            eaten_dog_position = ((current_position[0] + move[0]) // 2, (current_position[1] + move[1]) // 2)

            board[eaten_dog_position[0]][eaten_dog_position[1]] = '0'

            board[move[0]][move[1]] = '2'
            board[current_position[0]][current_position[1]] = '0'
       
def get_game_over(board):
    quantity_dogs = 0
    
    for row in range(8):
        for col in range(5):
            if board[row][col] == '1':
                quantity_dogs += 1
    
    if quantity_dogs == 9:            
        return True
    else:
        False

def get_game_winner(board):
    if get_jaguar_position(board) in get_prison_zone():
        return True
    elif not get_possible_moves_jaguar(board)[0]:
        return True
    else:
        return False

def get_prison_zone():
    prison_zone_positions = [(5,2), (6,1), (6,2), (6,3), (7,1), (7,2), (7,3)]
    
    return prison_zone_positions

def max_value(board, depth, alpha, beta):
    if depth == 0:
        return 0

    value = float('-inf')
    for move in get_possible_moves_jaguar(board)[0]:
        value = max(get_position_board(move), min_value(board, depth - 1, alpha, beta))
        alpha = max(alpha, get_position_board(move))
        
        if beta <= alpha:
            break
        
    return value

def min_value(board, depth, alpha, beta):
    if depth == 0:
        return 0

    value = float('inf')
    for move in get_possible_moves_jaguar(board)[0]:
        value = min(get_position_board(move), max_value(board, depth - 1, alpha, beta))
        beta = min(beta, get_position_board(move))
        
        if beta <= alpha:
            break
        
    return value

def alpha_beta_search(board, depth):
    best_move = None
    max_value = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for move in get_possible_moves_jaguar(board)[0]:
        value = min_value(board, depth - 1, alpha, beta)
        
        if value > max_value:
            max_value = value
            best_move = move
            
        alpha = max(alpha, max_value)
        
    return best_move

current_player = 2
max_depth = 5

print("Tabuleiro Inicial".center(25))
print_board(board)

while True:
    if get_game_winner(board):
        print("\nVocê venceu!\n")
        break
    
    if get_game_over(board):
        print("\nVocê perdeu!\n")
        break
    
    if current_player == 1:
        print(f"\nPosição dos Cachorros = {get_dogs_position(board)}")
        print(f"Movimentos Possíveis Para os Cachorros = {get_possible_moves_dogs(board)}\n")
        
        selected_dog = int(input("Escolha Um Cachorro: "))
        row_dog = int(input("Escolha a Linha do Movimento: "))
        col_dog = int(input("Escolha a Coluna do Movimento: "))

        print()
        make_move_dogs(board, selected_dog, (row_dog, col_dog))
        
        print_board(board)
        
        current_player = 2
    else:
        print(f"\nPosição da Onça = {get_jaguar_position(board)}")
        print(f"Movimentos Possíveis Para a Onça = {get_possible_moves_jaguar(board)[0]}\n")
        
        while len(get_possible_moves_jaguar_eat_dog(board)) >= 1:
            best_move = alpha_beta_search(board, max_depth)
            print(f"Melhor movimento: {best_move}\n")
            
            make_move_jaguar(board, best_move)
            
            print_board(board)
        
        current_player = 1