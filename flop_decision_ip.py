"""
Module to return the GTO flop decision for the player in position
after running TexasSolver
args:
    hand: format CARDsuitCARDsuit, e.g. Ac5h or TsJd

A valid command line input would be:
python3 flop_decision_ip.py Td4c
"""
import json
import sys

f = open('output_result.json', 'r')
data = json.load(f)
MY_HAND =sys.argv[1]

def ip_flop_strategy(hand):
    strat = []
    all_ip_actions = data['strategy']['actions']
    try:
        action = data['strategy']['strategy'][hand]
    except KeyError:
        hand = hand[2:] + hand[:2]
        action = data['strategy']['strategy'][hand]
    for j in range(len(action)):
        strat.append(f'{all_ip_actions[j]} : {action[j]}')
    return strat

print(ip_flop_strategy(MY_HAND))
