import random #import function

#Beginning scores
score_c = 0
score_p = 0

#Intro
while True:
    print('=============')
    print('Welcome to the rock, paper, scissors')
    print("It's best to 3!!")
    print("A tie scores 0.")
    print('=============')

    print('Pick from the following.')

    #Main menu
    while True:
        print('1) ✊')
        print('2) 🤚')
        print('3) ✌️')
        print('4) Quit😢')

        #Main game
        try:
            pl = int(input('Please pick a move:')) #User inputs a move

            if pl == 4:
                 print("You quit the game, you're welcome anytime!!") #User can quit the game, fully exiting the game
                 exit()

            cpu = random.randint(1,3)

            print('You chose: ', pl) #Line 33 and 34 displays the user and cpu choice
            print('CPU chose: ', cpu)

            #Game logic
            if pl == cpu:
                print(f"Both players selected {pl}. It's a tie.")

            elif pl == 1:
                if cpu == 2:
                    print('CPU wins!')
                    score_c += 1

                else:
                    print('You win!')
                    score_p += 1

            elif pl == 2:
                if cpu == 1:
                    print('CPU chose rock. You win!')
                    score_p += 1

                else:
                    print('You got chopped.😔')
                    score_c += 1

            elif pl == 3:
                if cpu == 1:
                    print('You lose!')
                    score_c += 1
                else:
                    print('You win!')
                    score_p += 1
                
            #Check user/cpu score and diplayes
            if score_p == 3 or score_c == 3:
                print('')
                print('Final score board👇')
                print(f'Your score: {score_p}')
                print(f'CPU score: {score_c}')
                
                if score_p == 3:
                    print('You won!! 🎉')
                else:
                    print('Better luck next time. ')
                break 
            
        except ValueError:
            print('Invalid input, please try again.')
                

    play_again = input("Play again? (Y/N): ")    
    if play_again != "Y" and play_again.lower() != "y":
            print('You want to touch grass? Enjoy 🏡')
            break
    else:
            print('The game has reset, enjoy!')
            score_c: 0
            score_p: 0
        