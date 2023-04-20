# StreamlinedPokerSolver
Tools added outside of an open-source Poker solver (https://github.com/bupticybee/TexasSolver) for easier use

# To run the solver:
Edit the "input.txt" file in the TexasSolver directory to match your desired hand and bet sizings. Then run 

./run_solver.sh

My scripts only work for one street right now, but will extend to an entire hand in the future.

# Python solver modules
The python modules work with the solver to ouput the decisions you should make (for only one street at the time of writing).
Since solvers output obtuse results with a lot of extra information, these modules were designed to give a one-command output that is easy to read and understand, corresponding to the decisions you have made and the hand you hold. It is also perfect for analyzing one certain spot. Until I make this more robust, it will require multiple solver runs if you would like GTO answers to multiple streets; just edit the input.txt file to update the turn card and bet sizings.

flop_decision_ip.py is the module for the player in position;
flop_decision_oop.py is the module for the player out of position

# bb_profits_per_hand.ipynb
This module will analyze your profits per hand. Just download your Bovada or Ignition hand histories and move to this directory. Change the file path in the bb_profits_per_hand notebook near the top. Run all cells and you will see a dataframe of your hands with their ev in big blinds. 
