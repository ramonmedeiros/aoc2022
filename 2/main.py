#!/usr/bin/env python

WON = 6
DRAW = 3
LOST = 0

R = "Rock"
P = "Paper"
S = "Scissors"

CONVERT = {"A": R, "X": R,
           "B": P, "Y": P,
           "C": S, "Z": S}

CHOICE_TO_VALUE = {R: 1, P: 2, S: 3}

def resultForYou(oponent, you):

    cOponent = CONVERT[oponent]
    cYou = CONVERT[you]

    if cYou == cOponent:
        return DRAW + CHOICE_TO_VALUE[cYou]

    rockVsScissor = (cYou == R and cOponent == S)
    papperVsRock = cYou == P and cOponent == R
    scissorsVsPaper = cYou == S and cOponent == P

    if rockVsScissor or papperVsRock or scissorsVsPaper:
        return WON + CHOICE_TO_VALUE[CONVERT[you]]

    return LOST + CHOICE_TO_VALUE[CONVERT[you]]


with open("input", "r") as fd:
    lines = fd.read().splitlines()

total = 0
for line in lines:
    oponent, you = line.split()
    total += resultForYou(oponent, you)

print("Playing accord to the strategy " + str(total))

newStrategy = 0
for line in lines:
    oponent, you = line.split()
    cOponent = CONVERT[oponent]

    # lose
    your = ""
    if you == "X":
        if cOponent == R:
            your = S
        elif cOponent == P:
            your = R
        elif cOponent == S:
            your = P
        newStrategy += LOST + CHOICE_TO_VALUE[your]

    # draw
    elif you == "Y":
        newStrategy += DRAW + CHOICE_TO_VALUE[cOponent]

    # win
    elif you == "Z":
        if cOponent == R:
            your = P
        elif cOponent == P:
            your = S
        elif cOponent == S:
            your = R
        newStrategy += WON + CHOICE_TO_VALUE[your]
print("New strategy " + str(newStrategy))
