import random
import statistics as stats

def main(): #Brody
    #accepts no arguments
    #calls all functions
    #returns nothing
    print('Welcome to the Rolling Dice Game!')
    print('Would you like to play? (y/n)')
    play = input(':> ')
    if play.lower() == 'y':
        index = [] * 12
        for num in range(12):
            dice = roll_die()
            index.append(dice)
            
        print(index)
        print('-----Roll # 1-----')
        count = 1
        index_count = 0
        for num in range(9):
            print(f'Die	 {count}: {index[index_count]}')
            count = count + 1
            index_count = index_count + 1
            
        for num in range(3):
            print(f'Die	{count}: {index[index_count]}')
            count = count + 1
            index_count = index_count + 1
            
        number = find_mode(dice, index)
    elif play.lower() == 'n':
        print('\nRolling Dice Game Closed.')
        
    else:
        print('\nPlease enter a valid input.\n')
        main()

def output_dice(dice): #Brody
    #accepts dice
    #calls roll_die()
    #returns each die in a list
    pass

def roll_die(): #Brody
    #accepts no arguments
    #rolls an interger from 1-6
    #returns a random interger from 1-6
    dice = random.randint(1,6)
    return dice

def first_roll(): #Oliver
    #accepts no arguments
    #uses roll_die() to generate a list of 12 random intergers
    #returns a list of 12 random intergers
    pass

def count_frequency(dice, index): #Brody
    #accepts dice and index
    #finds how often the mode appears
    #returns how often the that target value occurs in the list
    find_mode = stats.mode(index)
    return find_mode

def find_mode(dice, index): #Brody
    #accepts dice and index
    #uses count_frequency(dice, number) to determine how often each number occurs
    #returns the mode
    find_mode = count_frequency(dice, index)
    print(f'The mode is: {find_mode}')

def list_unmatched_dice(dice): #Oliver
    #accepts dice
    #determines which dice need to be rerolled
    #returns a list of indexes to reroll
    pass

def reroll_one(dice, index): #Oliver
    #accepts dice and index
    #calls roll_die() to reroll that index
    #returns a new list with that index rerolled
    pass

def reroll_many(dice): #Oliver
    #accepts dice
    #calls list_unmatched_dice(dice) and reroll_one(dice, index) to reroll each die != the mode
    #returns a list of rerolled dice
    pass

