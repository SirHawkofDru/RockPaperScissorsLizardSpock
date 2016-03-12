# Rock Paper Scissors Lizard Spock

#rock crushes scissors
#rock crushes lizard
#paper covers rock
#paper disproves spock
#scissors cut paper
#scissors decapitates lizard
#lizard eats paper
#lizard poisons spock
#spock smashes scissors
#spock vapourizes rock
import random

options = {1: 'rock', 2: 'paper', 3:'scissors', 4:'lizard', 5: 'Spock'}
moves = ('rock', 'paper', 'scissors', 'lizard', 'Spock')
winner = {'rock': ('scissors', 'lizard'), 'paper': ('rock', 'spock'),
     'scissors': ('paper', 'lizard'), 'lizard': ('paper', 'spock'), 'spock': ('scissors', 'rock')}
rockwins = ('scissors', 'lizard')
paperwins = ('rock', 'spock')
scissorswins = ('paper', 'lizard')
lizardwins = ('paper', 'spock')
spockwins = ('scissors', 'rock')

def cpchoice():
    number = random.randint(1,5)
    choice = options[number]
    return choice

def playerchoice():
    choice = raw_input("Please enter your choice: ").lower()
    if choice in moves:
        return choice
    else:
        playerchoice()

def who_wins():
    cpu = cpchoice()
    player = playerchoice()
    if cpu == player:
        print "Draw"
        play_again()
    elif cpu in winner[player]:
        print "You Win"
        play_again()
    else:
        print "you lose"
        play_again()

def play_again():
    question = raw_input("Would you like to roll again? ").lower()
    if question == 'yes' or question == 'y':
        who_wins()
    else:
        print "Thank you for playing."
        exit(0)

who_wins()

#if cpu == player:
#    print "Its a draw!"
#elif player == 'rock' and cpu in rockwins:
#    print "You crush your opponent!"
#else:
#    print "You lose!"