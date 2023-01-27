import random, time, sys

def whoWins(player, computer):
    if player == computer:
        return 'tie'
    if (player == 'R' and computer == 'S') or (player == 'P' and computer == 'R') or (player == 'S' and computer == 'P'):
        return 'player'
    if (player == 'R' and computer == 'P') or (player == 'P' and computer == 'S') or (player == 'S' and computer == 'R'):
        return 'computer'

print('''Rock, Paper, Scissors by Brent Danley
- Rock beats Scissors
- Paper beats Rock
- Scissors beats Rock
''')

wins = 0
losses = 0
ties = 0
moves = {'P': 'PAPER', 'R': 'ROCK', 'S': 'SCISSORS'}

while True: # Keep playing until player (Q)uits
    while True: # Get player input until valid
        print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()
        
        if playerMove not in moves.keys():
            print('Type one of R, P, S, or Q.')
            continue
        else:
            break

    print('{} versus...'.format(moves[playerMove]))
    
    restPeriod = 0.25
    for x in range(1,4):
        time.sleep(restPeriod * 2 if x == 1 else restPeriod)
        print('{}...'.format(x))

    # Get computer move
    randomNumber = random.randint(1,3)
    computerMove = list(moves.keys())[randomNumber - 1]
    print(moves[computerMove])
    time.sleep(0.5)

    winner = whoWins(playerMove, computerMove)

    # Tie
    if winner == 'tie':
        print('It\'s a tie!')
        ties += 1
    # Win
    if winner == 'player':
        print('You win!')
        wins += 1
    # Loss
    if winner == 'computer':
        print('You lose!')
        losses += 1

    print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))