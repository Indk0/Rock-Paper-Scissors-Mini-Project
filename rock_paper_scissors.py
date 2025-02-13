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

    try:
        pl = int(input('Please pick a move:'))

        cpu = random.randint(1,3)

        print('You chose: ', pl)
        print('CPU chose: ', cpu)

        if pl == cpu:
            print(f"Both players selected {pl}. It's a tie.")
        elif pl == 1:
            if cpu == 2:
                print('CPU wins!')
            else:
                print('You win!')
        elif pl == 2:
            if cpu == 1:
                print('CPU chose rock. You win!')
            else:
                print('You got chopped.😔')
        elif pl == 3:
            if cpu == 1:
                print('You lose!')
            else:
                print('You win!')
        else:
            print("You quit the session, you're welcome anytime!!")

    except ValueError:
        print('Invalid input, please try pick between 1 and 4.')