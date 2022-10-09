import random

moves = ["Rock", "Paper", "Scissor"]
pCount = 0
cCount = 0

while not(input("Enter Stop to Quit: ") == "Stop"):
    player = input("Rock, Paper or Scissor?\n")
    computerMoves = moves[random.randint(0, 2)]
    print("Computer: ", computerMoves)
    if cCount == 5:
        cCount = 0
        pCount = 0
        print("You Lost!")
    if pCount == 5:
        cCount = 0
        pCount = 0
        print("You Win!")
    if player == computerMoves:
        print("Draw. Try Again!")
    else:
        if player == "Rock":
            if computerMoves == "Scissor":
                print("Have some mercy.")
                pCount += 1
                print("You: ", pCount)
                print("Computer: ", cCount)
            else:
                print("Try harder.")
                cCount += 1
                print("You: ", pCount)
                print("Computer: ", cCount)
        if player == "Scissor":
            if computerMoves == "Paper":
                print("Have some mercy.")
                pCount += 1
                print("You: ", pCount)
                print("Computer: ", cCount)
            else:
                print("Try harder.")
                cCount += 1
                print("You: ", pCount)
                print("Computer: ", cCount)
        if player == "Paper":
            if computerMoves == "Scissor":
                print("Try harder.")
                cCount += 1
                print("You: ", pCount)
                print("Computer: ", cCount)
            else:
                print("Have some mercy.")
                pCount += 1
                print("You: ", pCount)
                print("Computer: ", cCount)