import random

print('=============')
print('Welcome to the rock, paper, scissors')
print('=============')

print('Pick from the following.')

while True:

    print('1) ✊')
    print('2) 🤚')
    print('3) ✌️')
    print('4) Quit😢')

    pl = int(input('Please pick a move:'))

    cpu = random.randint(1,3)

    print('You chose: ', pl)
    print('CPU chose: ', cpu)

    if pl == cpu:
        print(f"Both players selected {pl}. It's a tie.")
        break
    elif pl == 1:
        if cpu == 2:
            print('CPU wins!')
            break
        else:
            print('You win!')
            break
    elif pl == 2:
        if cpu == 1:
            print('CPU chose rock. You win!')
            break
        else:
            print('You got chopped.😔')
            break
    elif pl == 3:
        if cpu == 1:
            print('You lose!')
            break
        else:
            print('You win!')
            break
    elif pl == 4:
        print("You quit the session, you're welcome anytime!!")
        break
    else:
        print('Invalid input, please try again.')

play_again = input("Play again? (Y/N): ")    
if play_again != Y and != y:
        print('You want to touch grass? Enjoy')
        