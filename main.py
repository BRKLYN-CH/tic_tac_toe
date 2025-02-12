def player_choice():
    try:
        player_1 = input("Pick a square(X or O): ")
    except ValueError:
        print("That is not a valid option")
    player_1 = player_1.title()
    try:
        player_2 = input("Pick a square(X or O): ")
    except ValueError:
        print("That is not a valid option")
    player_2 = player_2.title()
    print(player_1)
    print(player_2)

    user_input = input("X or O")
    user.is alpha
    while loop 



def players_score(scores):
    scores = {'Player 1': 0, 'Player 2': 0}
    scores['Player 1'] += 1
    scores['Player 2'] += 1
    print(scores)

"""
def check_winner(board, scores,):
    for row in board:
        if all row == X:
            return scores['Player 1 or 2'] += 1

    for column in board:
        if all column == X:
            return scores['Player 1 or 2'] += 1
"""
player_choice()