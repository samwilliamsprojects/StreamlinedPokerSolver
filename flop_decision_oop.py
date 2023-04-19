"""
Module to return the GTO strategy for the player out of position
after running TexasSolver
args:
    hand: format CARDsuitCARDsuit, e.g. Ac5h or TsJd
    flop_action: the action of the player in position. Values to 
    6 decimal points.
    e.g. 'CHECK' or 'BET 13.000000'

A valid command line entry would look like this:
python3 flop_decision_oop.py Ac5h 'BET 13.000000'

It would be easiest if you ran the flop_decision.py and simply copied
the values that it returns, as those are the only values that the solver has used
and it will give the correct decimal places
"""
import json
import sys

f = open('output_result.json')
data = json.load(f)
MY_HAND = sys.argv[1]
flop_ip_action = sys.argv[2]

def oop_flop_strategy(hand):
    strat = []
    all_oop_actions = data['childrens'][flop_ip_action]['actions']
    try:
        action = data['childrens'][flop_ip_action]['strategy']['strategy'][hand]
    except KeyError:
        hand = hand[2:] + hand[:2]
        action = data['childrens'][flop_ip_action]['strategy']['strategy'][hand]
    for j in range(len(action)):
        strat.append(f'{all_oop_actions[j]} : {action[j]}')
    return strat

print(oop_flop_strategy(MY_HAND))