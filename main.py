def player_choice():
    while True:
        player_1 = input("Player 1's choice, are you an X or an O: ")
        player_1 = player_1.title()
        if player_1.isalpha() is True:
            if player_1 == "X" or player_1 == "O":
                break
            else:
                continue
        else:
            continue
    while True:
        player_2 = input("Player 2's choice, are you an X or an O: ")
        player_2 = player_2.title()
        if player_2.isalpha() is True:
            if player_2 == "X" or player_2 == "O":
                break
            else:
                continue
        else:
            continue
    """
    Ask them where they want to go and implement it. 
    go to update board and have that check if the square is open
    """


def players_score(scores):
    scores = {'Player 1': 0, 'Player 2': 0, 'Draw': 0}
    scores['Player 1'] += 1
    scores['Player 2'] += 1
    print(scores)


"""
def check_winner(board, scores):
    for row in board:
        if all row == X:
            return scores['Player 1 or 2'] += 1

    for column in board:
        if all column == X:
            return scores['Player 1 or 2'] += 1

    for digainl in board == x:
"""

def main():
    """ 
    while loop
    player_choice
    update board
    show board
    check it won(break if won)
    repeat
    """