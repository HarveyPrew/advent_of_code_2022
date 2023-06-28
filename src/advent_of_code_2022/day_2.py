

def parseRounds(path):
    # Creating a list called rounds
    rounds = list()

    # parse through txt file to collect all the rounds
    with open(path) as f:
        for line in f:
            round = line.strip()
            rounds.append((round[0], round[2]))

    return rounds


def scoreOneRound(round):
    # Dictionary converting the oppenents move from letters
    # to assigned variables with given scores
    rock = 1
    paper = 2
    scissors = 3
    plays = {'A': rock, 'B': paper, 'C': scissors}

    # opponentPlay being the assigned variables
    opponentPlay = plays[round[0]]

    # Dictionary converting the outcome from letters
    # to assigned variables with given scores
    lose = 0
    draw = 3
    win = 6
    outcomes = {'X': lose, 'Y': draw, 'Z': win}

    outcome = outcomes[round[1]]

    # Dictionary of the opponents move and the value being
    # another dictionary with outcome and my given move.
    playForOutcome = {
        rock: {lose: scissors, draw: rock, win: paper},
        paper: {lose: rock, draw: paper, win: scissors},
        scissors: {lose: paper, draw: scissors, win: rock},
    }

    # Accessing my move for given outcome + opponent move
    myPlay = playForOutcome[opponentPlay][outcome]

    roundScore = myPlay + outcome

    return roundScore


def scoreRounds(rounds):
    # Summing all the scoreOneRound value in the rounds list
    totalScore = sum(scoreOneRound(round) for round in rounds)

    return totalScore
