import winsound
import random

# Global Variables
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

current_player = 'X'
winner = None
game_running = True


# Display Board Function
def display_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# Enter Move Function
def enter_move(board):
    try:
        player_input = int(input("Enter a number 1-9: \n"))
        if 1 <= player_input <= 9 and board[player_input - 1] == '-':
            board[player_input - 1] = current_player
        else:
            winsound.Beep(400, 100)
            print("Oops! Number out of range or spot already taken.")
    except Exception as e:
        winsound.Beep(400, 100)
        print(f"Something went wrong: {e}")


# Make List of Free Fields Function
def make_list_of_free_fields(board):
    free_fields = []
    for i in range(len(board)):
        if board[i] == '-':
            free_fields.append(i)
    return free_fields


# Victory Check Function
def victory_for(board, sign):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == sign:
            return True
    return False


# Draw Move Function (Computer Move)
def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) > 0:
        computer_move = random.choice(free_fields)
        board[computer_move] = 'O'


# Check for Draw Function
def check_draw(board):
    if '-' not in board:
        return True
    return False


# Switch Player Function
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


# Main Game Loop
while game_running:
    display_board(board)
    enter_move(board)

    # Check for win or draw after player's move
    if victory_for(board, current_player):
        display_board(board)
        print(f"Player {current_player} wins!")
        game_running = False
        break
    elif check_draw(board):
        display_board(board)
        print("It's a draw!")
        game_running = False
        break

    # Switch to the next player (computer's turn if necessary)
    switch_player()

    # If the current player is 'O', it's the computer's turn
    if current_player == 'O':
        draw_move(board)

        # Check for win or draw after computer's move
        if victory_for(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_running = False
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            game_running = False
            break

        # Switch back to player after computer's move
        switch_player()
