import random

print(' Welcome to Rock Paper Scissor Game!! ')
print(' Player VS Computer ')
while True:
    game = bool(input(' Press Enter to play!! '))
    if not game:
        break
    else:
        print( 'Please, press Enter to play the game ' )

player_score = 0
comp_score = 0
while True:
    computer = random.choice(['rock', 'paper', 'scissor'])
    while True:
        player_one = input('choose your option: ').lower()
        if player_one[0] in ['r', 'p', 's']:
            break
        else:
            print(' Invalid choice!! ')
    for choose in ['rock', 'paper', 'scissor']:
        if player_one[0] == choose[0]:
            player_one = choose
    print(f'player: {player_one}')
    print(f'computer: {computer}')
    if (player_one[0] == 'r' and computer[0] == 'p') or (player_one[0] == 's' and computer[0] == 'r') or (player_one[0] == 'p' and computer[0] == 's'):
        print('computer wins!!')
        comp_score += 1
    elif (player_one[0] == 'p' and computer[0] == 'r') or (player_one[0] == 'r' and computer[0] == 's') or (player_one[0] == 's' and computer[0] == 'p'):
        print('Player wins!!')
        player_score += 1
    else:
        print('It\'s a Tie!!')
    print(f'player Score: {player_score}')
    print(f'Computer score: {comp_score}')
    if player_score == 3:
        print('End of the game... Player Wins!!!!')
        break
    elif comp_score == 3:
        print('End of the game... Computer Wins!!!!')
        break

# play_again = input(' Want to Play Again? ')
# if play_again[0].lower() == 'y':
#     print(' Here we go Again!! ')
# elif play_again == '':
#     print(' Thanks for playing ')
#     break
# else:
#     print(' Thanks for playing ')
#     break
