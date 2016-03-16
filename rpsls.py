import random
import os

options = {1: 'rock', 2: 'paper', 3:'scissors', 4:'lizard', 5: 'spock'}
moves = ('rock', 'paper', 'scissors', 'lizard', 'spock')
winner = {'rock': ('scissors', 'lizard'), 'paper': ('rock', 'spock'),
          'scissors': ('paper', 'lizard'), 'lizard': ('paper', 'spock'), 
          'spock': ('scissors', 'rock')}
scores = {'Player': 0, 'CPU': 0, 'Draw': 0}

def cpchoice():
    number = random.randint(1,5)
    choice = options[number]
    return choice

def playerchoice():
    choice = raw_input("Please enter your choice: ").lower()
    if choice in moves:
        return choice
    elif choice == "quit":
        os.system('cls')
        print "The final scores are:"
        show_scores()
        os.system('pause')
        os.system('cls')
        exit(0)
    elif choice == "rules":
        print """
              rock crushes scissors
              rock crushes lizard
              paper covers rock
              paper disproves spock
              scissors cut paper
              scissors decapitates lizard
              lizard eats paper
              lizard poisons spock
              spock smashes scissors
              spock vapourizes rock
              """
        who_wins()
    else:
        who_wins()

def who_wins():
    show_scores()
    cpu = cpchoice()
    player = playerchoice()
    os.system('cls')
    if cpu == player:
        print "Your Opponent chose %s: It's a Draw" % cpu
        scores['Draw'] += 1
        who_wins()
    elif cpu in winner[player]:
        print "Your Opponent chose %s: You Win" % cpu
        scores['Player'] += 1
        who_wins()
    else:
        print "Your Opponent chose %s: You Lose" % cpu
        scores['CPU'] += 1
        who_wins()

def show_scores():
    print "Player: %i" % scores['Player']
    print "CPU: %i" % scores['CPU']
    print "Draws: %i" % scores['Draw']
    return

os.system('cls')
print """Welcome to Rock - Paper - Scissors - Lizard - Spock
To see the rules and find check what beats what, type 'rules' instead of making your choice.
Type 'quit' to exit the game.
"""
who_wins()