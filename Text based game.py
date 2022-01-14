import time

answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("""
WELCOME! LET'S START THE ADVENTURE

You are standing outside of your house and you see a women running towards you and asking for urgent shelter.

Will you provide shelter to him. (Yes / No)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\nAfter 2 minutes, the Police came to your house, and ask you that whether the miafa leader is in your house or not. Will you say (Yes / No)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nYou are an honest person. She was a miafa memeber\n")
        print("You win!!"        )


    elif ans2 in answer_no:
        print("\nWomen tried to stab you and u stopped her\n")
        print("Women asks you to join the miafa gang, Will You join?")
        ans3 = input(">>")
        if ans3 in answer_yes:
            print("You joined Miafa!\n")
            print("\n You were promoted to Leaders personal body guard congrats!\n")
            time.sleep(2)
            print("\n On some random day u get a bag of money which can feed u for Rest of your life and then you saw police chasing your boss")
            print("\n will You try to save her or flee with money, will you really try to save her\n")
            ans4 = ">>"
            if ans4 in answer_yes:
                print("\n Police takes u with her, GAMEOVER")
            elif ans4 in answer_no:
                print("\n You found the secret ending YOU WON THE Game!!\n")
            else:
                print("Bruh what u tryna say :<")
        elif ans3 in answer_no:
            print("She kills You game over!")
        else:
            print("Bruh what u tryna say :<")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

elif ans1 in answer_no:
    print("\nNow, she is trying to kill you. Will, you knock him down? (Yes / No)\n")

    ans5 = input(">>")

    if ans5 in answer_yes:
        print("\nCongrats! He was a miafa leader & You helped the police to catch him with your bravery.")

    elif ans5 in answer_no:
        print("\nSorry! You are dead. sHe was a miafa leader & She killed you. GAME OVER")

    else:
        print("\nYou typed the wrong input. GOODBYE!")

else:
    print("\nYou typed the wrong input. GOODBYE!")