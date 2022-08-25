# Establish empty board
game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

# Total wins
player1_wins = 0
player2_wins = 0

# Player name placeholders
player1_name = "Player 1"
player2_name = "Player 2"

# Define translation of coords
def process_coords(player_coords):
    board_coord_X = None
    board_coord_Y = None
    sum_x = 0
    sum_y = 0
    x = 1
    y = 1
    if ',' in player_coords:
        coord_list = player_coords.split(",")
    else:
        return 0
    coord_list[0] = int(coord_list[0])
    coord_list[1] = int(coord_list[1])

    while x <= 3:
        if coord_list[0] == x:
            board_coord_X = 0 + sum_x
            x += 1
            sum_x += 1
        else:
            x += 1
            sum_x += 1

    while y <= 3:
        if coord_list[1] == y:
            board_coord_Y = 0 + sum_y
            y += 1
            sum_y += 1
        else:
            y += 1
            sum_y += 1
    
    coord_list = [board_coord_X, board_coord_Y]
    return coord_list

# Places game piece on board
def place_piece(coords, piece):
    row = coords[0]
    col = coords[1]
    if game[row][col] != 0:
        return 'occupied'
    else:
        game[row][col] = piece

# Players take turns while updating game board
def take_turns(player1_name, player2_name):
    turn = 1
    player1_turns = [1, 3, 5, 7, 9]
    player2_turns = [2, 4, 6, 8]

    while turn <= 9:
        if turn in player1_turns:
            player1 = input(player1_name + "'s turn: ")
            coords = process_coords(player1)
            # Error checking
            if coords == 0:
                print("Invalid input. Please try again.")
                player1 = input(player1_name + "'s turn: ")
                coords = process_coords(player1)
            piece = 'x'
            result = place_piece(coords, piece)
            if result == 'occupied':
                print("That is not an empty space. Please re-enter.")
                turn += 0
            else:
                turn += 1
        elif turn in player2_turns:
            player2 = input(player2_name + "'s turn: ")
            coords = process_coords(player2)
            # Error checking
            if coords == 0:
                print("Invalid input. Please try again.")
                player2 = input(player2_name + "'s turn: ")
                coords = process_coords(player2)
            piece = 'o'
            result = place_piece(coords, piece)
            # Check if space is taken
            if result == 'occupied':
                print("That is not an empty space. Please re-enter.")
                turn += 0
            else:
                turn += 1
        print(game[0])
        print(game[1])
        print(game[2])
        board_check = check_for_win(piece)
        # End game after board is full
        if turn > 9 or board_check == 3:
            print("Game Over!")
            return

# Check for wins in various directions
def check_for_win(piece):
    # Horizontal win
    def horizontal_win(rowNumber):
        global player1_wins
        global player2_wins
        x = 0
        o = 0
        for i in game[rowNumber]:
            if i == 'x':
                x += 1
            elif i == 'o':
                o += 1
        if x == 3:
            print("Player 1 wins!")
            player1_wins += 1
            return x, player1_wins, player2_wins
        elif o == 3:
            print("Player 2 wins!")
            player2_wins += 1
            return o, player1_wins, player2_wins
        else:
            return None, player1_wins, player2_wins

    # Vertical win
    def vertical_win():
        global player1_wins
        global player2_wins
        x = 0
        o = 0
        if (game[0][0] == 'x' and game[1][0] == 'x' and game[2][0] == 'x') \
        or (game[0][1] == 'x' and game[1][1] == 'x' and game[2][1] == 'x') \
        or (game[0][2] == 'x' and game[1][2] == 'x' and game[2][2] == 'x'):
            print("Player 1 wins!")
            player1_wins += 1
            x = 3
            return x, player1_wins, player2_wins
        elif (game[0][0] == 'o' and game[1][0] == 'o' and game[2][0] == 'o') \
        or (game[0][1] == 'o' and game[1][1] == 'o' and game[2][1] == 'o') \
        or (game[0][2] == 'o' and game[1][2] == 'o' and game[2][2] == 'o'):
            print("Player 2 wins!")
            player2_wins += 1
            o = 3
            return o, player1_wins, player2_wins
        else:
            return None, player1_wins, player2_wins


    # Diagonal win
    def diagonal_win():
        global player1_wins
        global player2_wins
        x = 0
        o = 0
        if (game[0][0] == 'x' and game[1][1] == 'x' and game[2][2] == 'x') \
        or (game[2][0] == 'x' and game[1][1] =='x' and game[0][2] == 'x'):
            print("Player 1 wins!")
            player1_wins += 1
            x = 3
            return x, player1_wins, player2_wins
        elif (game[0][0] == 'o' and game[1][1] == 'o' and game[2][2] == 'o') \
        or (game[2][0] == 'o' and game[1][1] =='o' and game[0][2] == 'o'):
            print("Player 2 wins!")
            player2_wins += 1
            o = 3
            return o, player1_wins, player2_wins
        else:
            return None, player1_wins, player2_wins

    
    # Scan for horizontal win
    row1, player1_wins, player2_wins = horizontal_win(0)
    row2, player1_wins, player2_wins = horizontal_win(1)
    row3, player1_wins, player2_wins = horizontal_win(2)
    if row1 != None:
        return row1
    elif row2 != None:
        return row2
    elif row3 != None:
        return row3
    
    #Scan for vertical win
    colWin, player1_wins, player2_wins = vertical_win()
    if colWin != None:
        return colWin

    #Scan for diagonal win
    diagWin, player1_wins, player2_wins = diagonal_win()
    if diagWin != None:
        return diagWin
        
# Starts the game
def start_game():
    userInput = input("Type 'start' when ready, or 'exit' to quit: ")
    global player1_name
    global player2_name
    if userInput == "start":
        if player1_wins == 0 and player2_wins == 0:
            player1_name = input("Player 1, please enter your name: ")
            player2_name = input("Player 2, please enter your name: ")
            player1_name = player1_name.strip()
            player2_name = player2_name.strip()
        print("Game starting...\n")
        take_turns(player1_name, player2_name)
        restart_game(player1_name, player2_name, player1_wins, player2_wins)
    elif userInput == "exit":
        print("Exiting program...")
    else:
        print("Invalid.")
        start_game()

# Restart game
def restart_game(player1_name, player2_name, player1_wins, player2_wins):
    print("Total Score:", player1_name, player1_wins, " | ", player2_name, player2_wins)
    answer = input("Would you like to play again? yes/no: ")
    if answer == "yes":
        global game
        game = [[0, 0, 0],
	            [0, 0, 0],
	            [0, 0, 0]]
        start_game()
    elif answer == "no":
        print("Thanks for playing!")
        print(player1_name, "total wins:", player1_wins)
        print(player2_name, "total wins:", player2_wins)
    else:
        print("Invalid")
        restart_game(player1_name, player2_name, player1_wins, player2_wins)




# Welcome screen
print("\nWelcome to the Tic Tac Toe Game!\n")
print("Here is your empty board:\n")
print(game[0])
print(game[1])
print(game[2])
print("\nInstructions: Pieces are placed on the board using a 'row,col' pattern. Allowed values are '1', '2', and '3'.\n")
start_game()


    
        


