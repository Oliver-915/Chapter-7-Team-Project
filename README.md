Chapter-7-Team-Project
Program name: Ezee
Brody D, Oliver Albert

<Ezee> Description
The program is a dice simulation game. The goal is to role 12 dice as many times to get the same number.

Function 1 (main): \Accepts no arguments Calls all functions to play the number of games specified
Function 2 (outputdice(dice)): Accepts dice Outputs each die in the list
Function 3 (roll_die): Accepts no arguments Returns a random integer from 1 to 6
Function 4 (first_roll):]Accepts no arguments Uses roll_die to generate a list of 12 integers Returns a list of 12 random integers
Function 5 (count_frequency(dice, number): Accepts a list of 12 random integers and a target value Returns how often that target value occurs in the list
Function 6 (find_mode(dice)): Accepts a list of dice. Uses count_frequency(dice, number) to determine how often each number occurs. Returns the mode
Function 7 (list_unmatched_dice(dice)): Accepts a list of dice Determines which dice need rerolled Returns a list of indexes to reroll
Function 8 (reroll_one(dice, index)): Accepts a list of dice and an index. Uses roll_die to reroll that index Returns a new list with that index rerolled
Function 9 (reroll_many(dice)): Accepts a list of dice Calls list_unmatched_dice() and reroll_one() to reroll each die != the mode. Returns a list of rerolled dice.




Function Diagrams
contact_manager	<return_type: null>	author: Oliver Albert
argument:type	takes input from the user for ____	
time:integer	calculates ______	outputs ____
name:string	takes input for name ___	returns total

function name2	<return_type:>	author: Oliver Albert
argument:type	takes input from the user for ____	
time:integer	calculates ______	outputs ____
name:string	takes input for name ___	returns total

function name3	<return_type:>	author: Oliver Albert
argument:type	takes input from the user for ____	
time:integer	calculates ______	outputs ____
name:string	takes input for name ___	returns total

contact_search	<return_type: string>	author: Allen Le
takes input from the user for searching		
finds contacts and outputs it	outputs contacts	
returns name, number, address, email		

contact_edit	<return_type: no>	author: Allen Le
takes input from the user for changes		
changes in temp file and replaces contacts_txt	outputs changed contacts.txt file	
returns nothing		

contact_delete	<return_type: boolean>	author: Allen Le
takes input from contact_search		
removes input contacts_txt	outputs changed contacts.txt file	
takes input for name	returns conformation boolean	

function name7	<return_type:>	author: Oliver Albert
argument:type	takes input from the user for ____	
time:integer	calculates ______	outputs ____
name:string	takes input for name ___	returns total
