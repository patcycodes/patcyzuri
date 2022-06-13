import random

game_over = False
user_wins = 0

options = ['R', 'P', 'S']

# rock:R,paper:P,scissors:S
print("""WELCOME THIS IS A ROCK - PAPER - SCISSORS - GAME\nRules of the game:
    Paper beats Rock
    Rock beats Scissors
    Scissors beats Paper
    Tie happens when you play the same move as the computer
GAME STARTS NOW.....
R--> ROCK P-->PAPER S-->SCISSORS q--> QUIT""")

while not game_over:
    user_input = input('Play your move:\n')
    if user_input == 'q':
        print('GAME quitted.....')
        break

    random_number = random.randint(0, 2)
    # rock:o,paper:1,scissors:2
    user_wins += 1

    computer_pick = options[random_number]

    if user_input == 'R' and computer_pick == 'S':
        print('You won!')
        game_over = True
        print('Game has ended....')
    elif user_input == 'P' and computer_pick == 'R':
        print('You won!')
        game_over = True
        print('Game has ended....')
    elif user_input == 'S' and computer_pick == 'P':
        print('You won!')
        game_over = True
        print('Game has ended....')
    elif user_input == computer_pick:
        print('It is a tie!')
    else:
        if user_input not in options:
            print('not in options')
        else:
            print('You lose!')
    print(f"""
Computer Move: {computer_pick}
User Move: {user_input}
    """)