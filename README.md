Chapter-7-Team-Project
Program name: Ezee dice game
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

main()	<return_type:>	author: Brody
argument:type	takes input from the user for Nothing	
time:integer	calculates rolls	outputs nothing
name:string	takes input for name nothing	returns total

output_dice(dice)	<return_type:>	author: Brody
argument:type	takes input from the user for dice	
time:integer	calculates dice	outputs dice
name:string	takes input for name list	returns total

first_role()	<return_type:>	author: brody
argument:type	takes input from the user for none
time:integer	calculates 12	outputs none
name:string	takes input for name count	returns total

count_frequency(dice, number) <return_type:>	author: Brody
argument:type	takes input from the user for dice and number
time:integer	calculates frequency	outputs none
name:string	takes input for name nothing	returns total

find_mode(dice)	<return_type:>	author: Oliver
argument:type	takes input from the user for dice	
time:integer	calculates mode	outputs none
name:string	takes input for name nothing	returns total

list_unmatched_dice(dice) return_type:>	author: Oliver
argument:type	takes input from the user for dice
time:integer	calculates unmatched dice	outputs none
name:string	takes input for name none	returns total

reroll_one(dice, index)	<return_type:>	author: Oliver
argument:type	takes input from the user for dice and index	
time:integer	calculates one die	outputs none
name:string	takes input for name none	returns total

reroll_many(dice) <return_type:>	author: Brody
argument:type	takes input from the user for dice values	
time:integer	calculates reroles outputs none
name:string	takes input for name none	returns total

roll_die() <return_type:>	author: Brody
argument:type	takes input from the user for none
time:integer	calculates 12 roles	outputs none
name:string	takes input for name none	returns total

