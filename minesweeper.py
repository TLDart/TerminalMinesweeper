import random
def random_spawner(matrix):
    while True:
        line = random.choice([line for line in range(len(matrix))])
        cell = random.choice([cell for cell in range(len(matrix[0]))])

        if matrix[line][cell] != '*':
            matrix[line][cell] = '*'
            break

def matrix_spawner(lines, columns, item):
    board = []
    for i in range(lines):
        line = []
        for i in range(columns):
            line.append(item)
        board.append(line)
    return board

def index_generator(matrix):
    char_1 = 0
    index = ' |'
    for i in range(len(matrix[0])):
        index += str(char_1) + ' '
        char_1 += 1
        if char_1 == 10:
            char_1 = 0
    print(index)
def show_matrix(matrix):
    index_generator(matrix)
    borded_line = '  ' + ('-'* (len(matrix[0])* 2 - 1))
    print(borded_line)
    ln_nr = 0
    for line in matrix:
        print(ln_nr, end='|')
        for cell in line:
            print(cell, end= ' ')
        print()
        ln_nr += 1
        if ln_nr == 10:
            ln_nr = 0
    print(borded_line)

    #Lower Index
    index_generator(matrix)


def mine_spawner(mines, board):
    for i in range(mines):
        random_spawner(board)

def number_adder(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            mine_level = 0
            #Top right
            if i != 0 and j != (len(grid[i]) - 1):
                #print(grid[i - 1][j + 1], (i,j))
                if grid[i - 1][j + 1] == '*':
                    mine_level +=1
            #Top left
            if i !=0 and j != 0:
                #print(grid[i - 1][j - 1], (i,j))
                if grid[i - 1][j - 1] == '*':
                    mine_level +=1
            #Down Right
            if i != (len(grid) - 1) and j != (len(grid[i]) - 1):
                #print(grid[i + 1][j + 1], (i,j))
                if grid[i + 1][j + 1] == '*':
                    mine_level += 1
            #Down Left
            if i!= (len(grid) - 1) and j !=0:
                #print(grid[i + 1][j - 1], (i,j))
                if grid[i + 1][j - 1] == '*':
                    mine_level +=1
            #Down
            if i !=(len(grid) - 1):
                #print(grid[i + 1][j], (i,j))
                if grid[i + 1][j] == '*':
                    mine_level +=1
            #Up
            if i!=0:
                #print(grid[i - 1][j], (i,j))
                if grid[i - 1][j] == '*':
                    mine_level +=1

            #Mid-Right
            if j != (len(grid[i])-1):
                if grid[i][j + 1] == '*':
                    mine_level +=1

            #Mid- Left
            if j != 0:
                if grid[i][j - 1] == '*':
                    mine_level +=1

            #Change mine_level
            if grid[i][j] != '*':
                grid[i][j] = mine_level

def board_generator(mines, columns, lines):
    matrix = matrix_spawner(lines, columns, 0)
    mine_spawner(mines, matrix)
    number_adder(matrix)
    #show_matrix(matrix)
    return matrix

def difficulty():
    while True:
        try:
            level = int(input('Please Choose a Difficulty Level: 1-> Beginner / 2-> Intermediate / 3-> Hard: '))
            if level == 1 or level == 2 or level == 3 or level == 1337:
                break
            else:
                print('Invalid Input')
        except:
            print('Invalid Input')

    default = False
    #Beginner
    if level == 1:
        mines = 25
        columns = 15
        lines = 15
    #Intermediate
    if level == 2:
        mines = 70
        columns = 25
        lines = 20
    #Hard
    if level == 3:
        mines = 120
        columns = 55
        lines = 30

    #Developer Debug
    if level == 1337:
        mines = 1
        columns = 2
        lines = 2

    if default:
        mines = 25
        columns = 15
        lines = 15
    else:
        print('Invalid Input')

    return mines, columns, lines, level

def complete(player_board, original_matrix, mines_number):
    true_mines = 0
    for i in range(len(player_board)):
        for j in range(len(player_board[0])):
            if original_matrix[i][j] == '*' and player_board[i][j] =='M':
                true_mines += 1
    if true_mines == mines_number:
        return True
    return False

def mines_left(mines, player_board):
    mines_left = 0
    for i in range(len(player_board)):
        for j in range(len(player_board[0])):
            if player_board[i][j] == 'M':
                mines_left += 1
    return mines_left


def player_behavior(board):
    board_len_row = [i for i in range(len(board))]
    board_len_col = [i for i in range(len(board[0]))]
    while True:
        try:
            row = int(input('Row: '))
            if row in board_len_row:
                break
            else:
                print('Invalid Input')
        except:
            print('Invalid Input')

    while True:
        try:
            column = int(input('Column: '))
            if column in board_len_col:
                break
            else:
                print('Invalid Input')
        except:
            print('Invalid Input')

    while True:
        action = input('Action -> C for no mine -> M for mine  -> ? for ?: ')
        if action == 'C' or action == 'M' or action == '?':
            break
        else:
            print('Invalid Input')

    return row, column, action

def reveal0(i, j, grid, player_matrix):
            #Top right
            if i != 0 and j != (len(grid[0]) - 1):
                #print(grid[i - 1][j + 1], (i,j))
                if grid[i - 1][j + 1] != '*' and grid[i - 1][j + 1] != 'V':
                    player_matrix[i - 1][j + 1] = grid[i - 1][j + 1]
                if grid[i - 1][j + 1] == 0:
                    #grid[i - 1][j + 1] = 'V'
                    #reveal0(i - 1, j + 1, grid, player_matrix)
                    pass

            #Top left
            if i !=0 and j != 0:
                #print(grid[i - 1][j - 1], (i,j))
                if grid[i - 1][j - 1] != '*' and grid[i - 1][j - 1] != 'V':
                    player_matrix[i - 1][j - 1] = grid[i - 1][j - 1]
                if grid[i - 1][j - 1] == 0:
                    #grid[i - 1][j - 1] = 'V'
                    #reveal0(i - 1, j - 1, grid, player_matrix)
                    pass

            #Down Right
            if i != (len(grid) - 1) and j != (len(grid[0]) - 1):
                #print(grid[i + 1][j + 1], (i,j))
                if grid[i + 1][j + 1] != '*' and grid[i + 1][j + 1] != 'V':
                    player_matrix[i + 1][j + 1] = grid[i + 1][j + 1]
                if grid[i + 1][j + 1] == 0:
                    #grid[i + 1][j + 1] = 'V'
                    #reveal0(i + 1, j + 1, grid, player_matrix)
                    pass

            #Down Left
            if i!= (len(grid) - 1) and j !=0:
                #print(grid[i + 1][j - 1], (i,j))
                if grid[i + 1][j - 1] != '*' and grid[i + 1][j - 1] != 'V':
                    player_matrix[i + 1][j - 1] = grid[i + 1][j - 1]
                if grid[i + 1][j - 1] == 0:
                    #grid[i + 1][j - 1] = 'V'
                    #reveal0(i + 1, j - 1, grid, player_matrix)
                    pass

            #Down
            if i !=(len(grid) - 1):
                #print(grid[i + 1][j], (i,j))
                if grid[i + 1][j] != '*' and grid[i + 1][j] != 'V':
                    player_matrix[i + 1][j] = grid[i + 1][j]
                if grid[i + 1][j] == 0:
                    grid[i + 1][j] = 'V'
                    reveal0(i + 1, j, grid, player_matrix)
            #Up
            if i!=0:
                #print(grid[i - 1][j], (i,j))
                if grid[i - 1][j] != '*' and grid[i - 1][j] != 'V':
                    player_matrix[i - 1][j] = grid[i - 1][j]
                if grid[i - 1][j] == 0:
                    grid[i - 1][j] = 'V'
                    reveal0(i - 1, j, grid, player_matrix)

            #Mid-Right
            if j != (len(grid[0])-1):
                if grid[i][j + 1] != '*' and grid[i][j + 1] != 'V':
                    player_matrix[i][j + 1] = grid[i][j + 1]
                if grid[i][j + 1] == 0:
                    grid[i][j + 1] = 'V'
                    reveal0(i, j + 1, grid, player_matrix)

            #Mid-Left
            if j != 0:
                if grid[i][j - 1] != '*' and grid[i][j - 1] != 'V':
                    player_matrix[i][j - 1] = grid[i][j - 1]
                if grid[i][j - 1] == 0:
                    reveal0(i, j - 1, grid, player_matrix)



def game_engine(board, mines_number, Difficulty):
    game_over = False
    moves = 0
    player_matrix = matrix_spawner(len(board), len(board[0]),'.')
    show_matrix(player_matrix)
    while not complete(player_matrix, board, mines_number):
        print('Mines Left : {}'.format(mines_number - mines_left(mines_number, player_matrix)))

        rd = player_behavior(board)
        #Case 1 no mine
        if rd[2] == 'C':
            if board[rd[0]][rd[1]] == '*':
                game_over = True
                break

            if board[rd[0]][rd[1]] == 0:
                reveal0(rd[0],rd[1], board, player_matrix)
            else:
                player_matrix[rd[0]][rd[1]] = board[rd[0]][rd[1]]

        if rd[2] == 'M':
            if player_matrix[rd[0]][rd[1]] == '.' or player_matrix[rd[0]][rd[1]] == 'M':
                if player_matrix[rd[0]][rd[1]] == 'M':
                     player_matrix[rd[0]][rd[1]] = '.'
                else:
                    player_matrix[rd[0]][rd[1]] = 'M'
            else:
                pass

        if rd[2] == '?':
            if player_matrix[rd[0]][rd[1]] == '.' or  player_matrix[rd[0]][rd[1]]== '?':
                if player_matrix[rd[0]][rd[1]]== '?':
                    player_matrix[rd[0]][rd[1]] = '.'
                else:
                    player_matrix[rd[0]][rd[1]]= '?'
            else:
                pass

        moves +=1
        show_matrix(player_matrix)
        #print(complete(player_matrix, board, mines_number))

    if game_over is True:
        game_Lost(board)
    else:
        Victorious(Difficulty, moves, board)

def game_reset():
    while True:
        answer = input('Would you like to play again? Press y to continue.')
        if answer == 'y' or answer == 'Y':
            break
    minesweeper()

def Victorious(difficulty, moves,board):
    dict = {1: 'Beginner', 2:'Intermediate', 3: 'Hard', 4:'Insane', 1337:'XxMLGProNoobSlayerxX'}
    print('Congratulations!You have finished a Game in {}  with {} moves'.format(dict[difficulty], moves))
    show_matrix(board)

    game_reset()

def game_Lost(board):
    print('Game Over')
    for line in range(len(board)):
        for cell in range(len(board[line])):
            if board[line][cell] == 'V':
                board[line][cell] = 0
    show_matrix(board)
    game_reset()

def minesweeper():
    difficulty_ = difficulty()
    mines = difficulty_[0]
    columns = difficulty_[1]
    lines = difficulty_[2]
    level = difficulty_[3]
    print('Welcome to Minesweeper')
    game_board = board_generator(mines, columns, lines)
    game_engine(game_board, mines, level)


minesweeper()
