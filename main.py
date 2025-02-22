game_board = [
    ["-","-","-",],
    ["-","-","-"],
    ["-","-","-"]
]
different_board = [
    ["1","2","3",],
    ["4","5","6"],
    ["7","8","9"]
]

scores = {'Player 1': 0, 'Player 2': 0}

def player_scores(scores):
    print(scores)

def print_current_board():
    for row in range(len(game_board)):
        for column in range(len(game_board[row])):
            print(f"{game_board[row][column]:<5}", end = "")
        print("")

def print_different_board():
    for row in range(len(different_board)):
        for column in range(len(different_board[row])):
            print(f"{different_board[row][column]:<5}", end = "")
        print("")

def check_for_winner(game_board):
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != "-":
            return True
        if game_board[0][i] == game_board[1][i] == game_board[2][i] != "-":
            return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "-" or game_board[0][2] == game_board[1][1] == game_board[2][0] != "-":
        return True
    return False

def check_for_draw(game_board):
    for row in game_board:
        if "-" in row:
            return False
    return True

def player_choice(game_board):
    print_current_board()
    while True:
        player_1 = input("Player 1, choose X or O: ")
        player_1 = player_1.upper()
        if player_1.isalpha() is True:
            if player_1 == "X" or player_1 == "O":
                break
            else:
                continue
        else:
            continue
    if player_1 == "X":
        player_2 = "O"
    else:
        player_2 = "X"
    print(f"Player 1 is {player_1} and Player 2 is {player_2}")

    print_different_board()

    while not check_for_winner(game_board) and not check_for_draw(game_board):
        while True:
            player_one = int(input("Player 1, enter the number for the spot you want: "))
            row = (player_one - 1) // 3
            column = (player_one - 1) % 3
            if game_board[row][column] == "-":
                game_board[row][column] = player_1
                break
            else:
                print("That spot is taken, try again:")

        print_current_board()

        if check_for_winner(game_board):
            print("Player 1 wins!")
            scores['Player 1'] += 1
            return
        if check_for_draw(game_board):
            print("It's a draw!")
            return

        while True:
            player_two = int(input("Player 2, enter the number for the spot you want: "))
            row = (player_two - 1) // 3
            column = (player_two - 1) % 3
            if game_board[row][column] == "-":
                game_board[row][column] = player_2
                break
            else:
                print("That spot is taken, try again:")

        print_current_board()

        if check_for_winner(game_board):
            print("Player 2 wins!")
            scores['Player 2'] += 1
            return
        if check_for_draw(game_board):
            print("It's a draw!")
            return

def main():
    while True:
        player_choice(game_board)
        player_scores(scores)
        for i in range(3):
            for j in range(3):
                game_board[i][j] = "-"

if __name__ == "__main__":
    main()