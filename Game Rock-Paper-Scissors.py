import random

def select_and_print_selection(player):
    selection = random.randint(0, 2)
    print(f"Player {player} selected: {selection, options[selection]}")
    return selection

options = {
    0: "rock",
    1: "scissor",
    2: "paper",
}

cases = {
    (0, 1): 1,
    (1, 2): 1,
    (2, 0): 1,
    (1, 0): 2,
    (2, 1): 2,
    (0, 2): 2,
}
count1, count2 = 0, 0
player1, player2 = 0, 0

while count1 <3 and count2 <3:
    player1 = select_and_print_selection(1)
    player2 = select_and_print_selection(2)

    if player1 != player2:
        if cases[(player1, player2)] == 1:
            count1 += 1
            print(f"Player {cases[(player1, player2)]} won this round.!")

        else:
            count2 += 1
            print(f"Player {cases[(player1, player2)]} won this round.!")

    else:
        print("Draw!")

print(f"Player 1 score is {count1}")
print(f"Player 2 score is {count2}")

if count1 == 3:
    print(f"Player 1 won game.")

else:
    print(f"Player 2 won game.")



