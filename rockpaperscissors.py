p1_win = (1,0)
p2_win = (0,1)
draw = (0,0)
char_points = {"R": 0, "P": 1, "S": 2}

payout_matrix = [
    [draw, p2_win, p1_win],
    [p1_win, draw, p2_win],
    [p2_win, p1_win, draw]
]

sp1 = 0
sp2 = 0
score = [int(sp1), int(sp2)]
print("ROCK PAPER SCISSORS")
play = input("Play? - Y/N: ")

while play != "N":
    print("Choose a play [R, P, S]")
    p1 = str(input("P1: "))
    while p1 not in char_points.keys():
        p1 = str(input("P1 (try again retard! - [R, P, S]): "))
    p2 = str(input("P2: "))
    while p2 not in char_points.keys():
        p2 = str(input("P1 (try again retard! - [R, P, S]): "))
    p1_index = char_points.get(p1)
    p2_index = char_points.get(p2)
    payout = payout_matrix[p1_index][p2_index]
    if payout == draw:
        print("Draw!")
    elif payout == p1_win:
        print("Player 1 Wins!")
    elif payout == p2_win:
        print("Player 2 Wins!")
    sp1 = sp1 + payout[0]
    sp2 = sp2 + payout[1]
    print("Scores - P1: {sp1}, P2: {sp2}".format(sp1=sp1, sp2=sp2))
    play = input("Play again? - Y/N: ")

print("Goodbye!")
