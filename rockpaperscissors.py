char_points = {"R": 1, "P": 2, "S": 3}
sp1 = 0
sp2 = 0
score = [int(sp1), int(sp2)]
print("ROCK PAPER SCISSORS")
play = input("Play? - Y/N: ")

while play != "N":
    play1 = "Y"
    while play1 != "N":
        print("Choose a play//R, P, S//")
        p1 = str(input("P1: "))
        p2 = str(input("P2: "))
        p11 = char_points.get(p1)
        p12 = char_points.get(p2)

        if p11 == p12:
            print("Draw!")
        else:
            if p11 + p12 == 3 and p11 > p12:
                print("Player 1 Wins!")
                sp1 += 1
                print(str(score))
            else:
                if p11 + p12 == 3 and p11 < p12:
                    print("Player 2 Wins!")
                    sp2 += 1
                    print(str(score))
            if p11 + p12 == 4 and p11 > p12:
                print("Player 2 Wins!")
                sp2 += 1
                print(str(score))
            else:
                if p11 + p12 == 4 and p11 < p12:
                    print("Player 1 Wins!")
                    sp1 += 1
                    print(str(score))
            if p11 + p12 == 5 and p11 > p12:
                print("Player 1 Wins!")
                sp1 += 1
                print(str(score))
            else:
                if p11 + p12 == 5 and p11 < p12:
                    print("Player 2 Wins!")
                    sp2 += 1
                    print(str(score))
        play1 = input("Play Again? - Y/N: ")

        while quit != "sore loser":
            quit = input("Type sore loser to rage quit: ")
            quit = input("Try again loser: ")
            print("/Run/Self_Destruct - Y/N \n 5 \n 4 \n 3 \n 2\n 1")