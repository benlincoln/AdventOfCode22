import sys

from usefulFunctions.usefulFunctions import getFileConts

# Pass the path to the data of choice and get the answer!

if __name__ == '__main__':
    pathToFile = sys.argv[1]
    games = getFileConts(pathToFile).split('\n')
    options = [ {'move': 'rock',  'aliases':['A','X'], 'weakTo':'paper', 'value' : 1},
               {'move': 'paper', 'aliases':['B','Y'], 'weakTo': 'scissors', 'value': 2},
               {'move': 'scissors','aliases':['C','Z'], 'weakTo':'rock', 'value' : 3}
               ]
    scoreP1 = 0
    scoreP2 = 0
    for game in games:
        playerChoices = game.split(' ')
        opp = playerChoices[0]
        you = playerChoices[1]
        for key in options:
            if opp in key.get('aliases'):
                opp = key
            if you in key.get('aliases'):
                you = key
        scoreP1 += you['value']
        # Draw
        if opp == you:
            scoreP1 += 3
        if opp['weakTo'] == you['move']:
            scoreP1 += 6
        # Don't even need to include a statement for loss as it does not add any score
        oppP2 = playerChoices[0]
        youP2 = playerChoices[1]
        for key in options:
            if oppP2 in key.get('aliases'):
                oppP2 = key
        if youP2 == 'Y':
            youP2 = oppP2
        if youP2 in ['X', 'Z']:
            for key in options:
                if youP2 == 'X' and key != oppP2 and key['move'] != oppP2['weakTo']:
                    youP2 = key
                if youP2 == 'Z' and key['move'] == oppP2['weakTo']:
                    youP2 = key
        scoreP2 += youP2['value']
        # Draw
        if oppP2 == youP2:
            scoreP2 += 3
        if oppP2['weakTo'] == youP2['move']:
            scoreP2 += 6
    print(f'Your total score from {len(games)} total games was {scoreP1} in part 1')
    print(f'Your total score from {len(games)} total games was {scoreP2} in part 2')




