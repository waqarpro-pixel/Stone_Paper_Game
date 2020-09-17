import random as rt
choose = ["rock","paper","scissor"]

comp = choose[rt.randint(0,2)]

player = True
print("\t\t\t\t\tRock Paper Scissor")
while player:
    player = input("Choose the Option")
    if player == comp:
        print("Tie")
    elif player == "rock":
        if comp == "paper":
            print("You lose Because Computer has",comp)
        else:
            print("You Win Because Computer has",comp)
    elif player == "scissor":
        if comp == "rock":
            print("You lose Because Computer has",comp)
        else:
            print("You Win Because Computer has",comp)
    elif player == "paper":
        if comp == "scissor":
            print("You lose Because Computer has",comp)
        else:
            print("You Win Because Computer has",comp)
    else:
        print("You don't Play")
        player == False