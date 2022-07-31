import numpy
run_game = True
board = {
	'topleft': ' ', 'topmid': ' ', 'topright':' ',
        'midleft': ' ', 'midmid': ' ', 'midright': ' ',
        'downleft': ' ', 'downmid': ' ', 'downright': ' ',
        'marble': 'X'
	}

def board_keys():
    # return the keys values of the board i.e topleft, topmid,......,
    global board
    keys = [key.lower() for key in board.keys()]
    print(keys)
    return keys

def printBoard(board):
    #print the board 
    print(board['topleft'], '|', board['topmid'], '|', board['topright'])
    print('- + - + -')
    print(board['midleft'], '|', board['midmid'], '|', board['midright'])
    print('- + - + -')
    print(board['downleft'], '|', board['downmid'], '|', board['downright'])

def marble():
    # plyer object
    global board
    if board['marble'] ==  'X':
        board['marble'] = 'O'
    else:
        board['marble'] = 'X'
    return board['marble']
    #see whether their is a better way to code in this format
    #marble = (board['marble'] =="X") ? board['marble'] = "O": board['marble'] = 'X'


def players_first_moves():
    # player first moves
    global board
    while True:
        printBoard(board)
        board_keys()
        move = input("Enter your move: ")
    #come back and check for validiy
        if move.lower() not in board_keys():
            print('invalid input!!! use the values above (eg: topleft ')
            continue
        if board[move.lower()].isspace():
            board[move.lower()] = marble()
            break
        elif board[move.lower()].isalpha():
            print('!place selected filled!')
            continue
        

def check_win():
    # check who win the game 
    # returns a turple of the return values if true
    # the 1 in the code means True and 0 means False since bool is subscriptable
    global board
    if board['topleft'].strip() == board['topmid'].strip() and board['topleft'].strip() == board['topright'].strip() and board['topleft'].strip().isalpha():
        return board['topleft'] 
    elif board['topleft'].strip() == board['midmid'].strip() and board['topleft'].strip() == board['downright'].strip() and board['topleft'].strip().isalpha():
        return board['topleft']
    elif board['topright'].strip() == board['midmid'].strip() and board['topright'].strip() == board['downleft'].strip() and board['downleft'].strip().isalpha():
        return board['topright']
    elif board['midright'].strip() == board['midmid'].strip() and board['midright'].strip() == board['midleft'].strip() and board['midleft'].strip().isalpha():
        return board['midright']
    elif board['downright'].strip() == board['downmid'].strip() and board["downleft"].strip() == board['downright'].strip() and board['downright'].strip().isalpha():
        return board['downright']
    elif board['topright'].strip() == board['midright'].strip() and board['topright'].strip() == board['downright'].strip() and board['topright'].strip().isalpha():
        return board['topright']
    elif board['topmid'].strip() == board['midmid'].strip() and board["topmid"].strip() == board['downmid'].strip() and board['topmid'].strip().isalpha():
        return board['topmid']
    elif board['topleft'].strip() == board['midleft'].strip() and board['topleft'].strip() == board['downleft'].strip() and board['topleft'].strip().isalpha():
        return board['topleft']
 

def select_marble():
    # select marble  to move
    global board
    while True:
        printBoard(board)
        board_keys()
        #come back and check for input validity
        selected_moving_marble = input('select marble to move: ')
        if board[selected_moving_marble].strip().isalpha():
            return selected_moving_marble
            break
        else:
            print('invalied input! No marble')
            continue

def move_marble_to(selected_marble):
    #move the marble to a specific location after been selected
    global board
    while True:
        printBoard(board)
        board_keys()
        print('Enter the position to move marble to')
        move_to = input()
        if board[move_to].strip().isalpha():
            print("invalid! place filed")
            continue
        else:
            board[move_to] = board[selected_marble]
            board[selected_marble] = ' '
            break
def do_if_checkwin():
    global run_game
    # what to do after checking for a win
    if check_win() != None: 
            print(check_win(), 'win !!!')
            play_again = input("Do you want to play again? y/n: ")
            if play_again.lower() != 'y' or play_again.lower().lower() != "yes":
                run_game = False

def game_main():
    game_run_number = 1
    global run_game
    while run_game:
        while game_run_number <=6:
            players_first_moves()
            break
            
        if game_run_number >= 6:
            selected_marble = select_marble()
            move_marble_to(selected_marble)
        do_if_checkwin()
        game_run_number +=1

game_main()
