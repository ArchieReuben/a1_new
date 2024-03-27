# DO NOT modify or add any import statements
from typing import Optional
from a1_support import *

# Name:
# Student Number: 
# ----------------

# Write your classes and functions here
def num_hours() -> float:
    #Program to display total hours spent on assignment
    duration = 4
    return float(duration)

# def check_input(command: str) -> bool:
#         if(len(command)>0):
#              action = command[0]

def generate_initial_board() -> list[str]:
    #Display an empty board consisting of eight rows and eight columns
    column = [BLANK_PIECE] * BOARD_SIZE
    column = ''.join(column)
    board_state = []
    for i in range(BOARD_SIZE):
        board_state.append(column)
    return board_state
    ##board_state = ['--------', '--------', '--------', '--------', '--------', '--------',
    ##'--------', '--------']
    ##return board_state


def is_column_full(column: str) -> bool:
    if(column[0] != "-"):
        return True
    else:
        return False
    
def is_column_empty(column):
    if(column[BOARD_SIZE-1] == '-'):
        return True
    else:
        return False
        
board_state = generate_initial_board() #main

def display_board(board_state) -> None:
    for column in range(BOARD_SIZE):
        row = "" + COLUMN_SEPARATOR
        for n in board_state:
            row = row + n[column] + COLUMN_SEPARATOR
        print(row)
    print(" 1 2 3 4 5 6 7 8 ")

def check_input(command: str) -> bool:
    move_input = ['A', 'a', 'R', 'r']
    req_input = ['Q', 'q', 'H', 'h']
    if command == "":
        ############ edit this function ###############
        print(INVALID_FORMAT_MESSAGE)
        return False
    elif len(command) > 2:
        print(INVALID_FORMAT_MESSAGE)
        return False
    elif len(command) == 1:
        if command in req_input:
            return True
        else:
            print(INVALID_FORMAT_MESSAGE)
            return False
        
    elif command[0] not in move_input:
        print(INVALID_FORMAT_MESSAGE)
        return False
    
    elif command[0] in req_input:
        return True

    elif command[0] in move_input and command[1] in '12345678':
        return True
    else:
        print(INVALID_COLUMN_MESSAGE)
        return False        

def switch_player(piece):
    piece == True
    piece = PLAYER_1_PIECE
    if(active_player == 1):
        active_player = 2
        piece = PLAYER_2_PIECE
    else:
        active_player = 1
        piece = PLAYER_1_PIECE

def player_turn_msg(active_player):
        if(active_player == 1):
            return PLAYER_1_MOVE_MESSAGE
        else:
            return PLAYER_2_MOVE_MESSAGE
'''  
def check_column_valid(command: str) -> bool:
        if(len(command) == 2):
            try:
                column = int(command[1])
                column_range = range(1,9)
                if(column in column_range):
                    return True
                else:
                    print(INVALID_COLUMN_MESSAGE)
                    return False
            except:
                print(INVALID_COLUMN_MESSAGE)
                return False
        else:
            print(INVALID_COLUMN_MESSAGE)
            return False
'''
def get_action() -> str:
    game_active = 1
    while game_active == 1:
        command  = input(ENTER_COMMAND_MESSAGE)
        if check_input(command) is False:
            continue
        else:
            game_active+=1
            return command
        
    print("Thanks for playing.")

def add_piece(board_state: list[str], piece: str, column_index: int) -> bool:
    c = (board_state[column_index])
    if  is_column_full(c):
        print(FULL_COLUMN_MESSAGE)
        return False
    if  is_column_empty(c):
       column = ""
       column = BLANK_PIECE*7 + piece
       board_state[column_index]=column
       return True
    else:
        column = board_state[column_index]
        gap_index = column.rfind(BLANK_PIECE)
        if gap_index != -1:
            column = column[:gap_index] + piece + column[gap_index+1:]
            board_state[column_index] = column
            return True
        else:
            print(FULL_COLUMN_MESSAGE)
            return False
        
def remove_piece(board_state: list[str], column_index: int) -> bool:
    column = board_state[column_index]
    if is_column_empty(board_state[column_index]):
        print(EMPTY_COLUMN_MESSAGE)
        return False
    else:
        new_column=''
        new_column = BLANK_PIECE + column[0:BOARD_SIZE-1]
        board_state[column_index] = new_column
        return True
    
def check_win(board_state: list[str]) -> Optional[str]:
    player_1_win = 0
    player_2_win = 0
    #vert
    for column in board_state:
        if PLAYER_1_PIECE*4 in column:
            player_1_win += 1
        if PLAYER_2_PIECE*4 in column:
            player_2_win += 1

    #horizontal
    for n in range(BOARD_SIZE):
        row = ''
        for i in board_state:
            row +=i[n]
        if 'XXXX' in row:
            player_1_win += 1
        if 'OOOO' in row:
            player_2_win += 1

    #diagonal
    r=3
    starting_row = 3
    while r <= 7 :
        c = 0
        diagonal=''
        while r >= 0:
            diagonal+=board_state[c][r]
            c+=1
            r-=1
        if "XXXX" in diagonal:
             player_1_win += 1
        if "OOOO" in diagonal:
            player_2_win += 1
        starting_row += 1
        r = starting_row
    
    c = 1
    starting_row = 1
    while c <= 4:
        diagonal = ''
        r = 7
        while c <= 7:
            diagonal += board_state[c][r]
            c += 1
            r -= 1
        if 'XXXX' in diagonal:
            player_1_win += 1
        if 'OOOO' in diagonal:
            player_2_win += 1
        starting_row +1
        c = starting_row

    
    r=4 
    starting_row = 4
    while r > 0:
        c=0
        diagonal = ""
        while r <=7:
            diagonal += board_state[c][r]
            r = r+1
            c = c+1
            if "XXXX" in diagonal:
                 player_1_win += 1
            if 'OOOO' in diagonal:
                player_2_win += 1
            starting_row -= 1
            r = starting_row
    c = 1
    starting_row = 1
    while c <= 4:
        r = 0
        while c <=7:
            diagonal += board_state[c][r]
            c = c+1
            r = r+1
            if "XXXX" in diagonal:
                 player_1_win += 1
            if 'OOOO' in diagonal:
                player_2_win += 1
            starting_row += 1
            c = starting_row

    if player_1_win > 0 and player_2_win > 0:
        print(DRAW_MESSAGE)
        return BLANK_PIECE
    elif player_1_win > 0:
        print(PLAYER_1_VICTORY_MESSAGE)
        return PLAYER_1_PIECE
    elif player_2_win > 0:
        print(PLAYER_2_VICTORY_MESSAGE)
        return PLAYER_2_PIECE

    
def play_game():
    piece = PLAYER_1_PIECE
    board_state = generate_initial_board()
    display_board(board_state)
    print(PLAYER_1_MOVE_MESSAGE)
    turn = 1 # player 1 turn is 1, and player 2 turn is 0
    while check_win(board_state) == None:
        input = get_action()
        if input in "Hh":
            print(HELP_MESSAGE)
            display_board(board_state)
            if turn == 1:
                print(PLAYER_1_MOVE_MESSAGE)
            else:
                print(PLAYER_2_MOVE_MESSAGE)
        if input in "Qq":
            break
        if input[0] in "Aa":
            column = int(input[1]) - 1
            add = add_piece(board_state, piece, column)
            if add is True:
                display_board(board_state)
                if check_win(board_state) == None:
                    if turn == 0:
                        print(PLAYER_1_MOVE_MESSAGE)
                        piece = PLAYER_1_PIECE
                        turn += 1
                    elif turn == 1:
                        print(PLAYER_2_MOVE_MESSAGE)
                        piece = PLAYER_2_PIECE
                        turn -= 1
                    else:
                        break


"""
    def check_column_valid(command: str) -> bool:
        if(len(command) == 2):
            command 
"""

def main() -> None:
    display_board(board_state)
    get_action()
    """The main function"""

if __name__ == "__main__":
    main()
