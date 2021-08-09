import random, sys

print('Rock,Paper, Scissors')

wins = 0
losses = 0
ties = 0

while True: #main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # Player input loop
        playerMove = '' # stores players move as empty for the next loop which validates input
        while playerMove != 'r' or playerMove != 'p' or playerMove != 's' or playerMove != 'q':
            print('Enter your move (r)ock (p)aper (s)cissors or (q)uit')
            playerMove = input()
            if playerMove == 'r' or playerMove == 'p' or playerMove == 's' or playerMove == 'q':
                if playerMove == 'q':
                        sys.exit() # quit on q input
                break
        computer_move = random.randint(0,2)
        comp_moves = ['r','p', 's']
        print('You: ' + playerMove + ' |vs| Computer: '+ comp_moves[computer_move])
        # Display and record the win/loss/tie:
        if playerMove == comp_moves[computer_move]:
            print('It is a tie!')
            ties = ties + 1
        elif playerMove == 'r' and comp_moves[computer_move] == 's':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'p' and comp_moves[computer_move] == 'r':
            print('You win!')
            wins = wins + 1
        elif playerMove == 's' and comp_moves[computer_move] == 'p':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'r' and comp_moves[computer_move] == 'p':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 'p' and comp_moves[computer_move] == 's':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 's' and comp_moves[computer_move] == 'r':
            print('You lose!')
            losses = losses + 1
