import random
import statistics as stats

def main():
    #accepts no arguments
    #calls all functions
    #returns nothing
    print('Welcome to Ezee!')
    print('Would you like to play? (y/n)')
    play = input(':> ')
    if play.lower() == 'y':
        index = [] * 12
        for num in range(12):
            dice = roll_die()
            index.append(dice)
        asdasdasdasd = output_dice(dice, index)
        
        number = find_mode(dice, index)
        print(f'The mode is {number}')
        
        reroll = list_unmatched_dice(dice, index, number)
        
    elif play.lower() == 'n':
        print('\nEzee Closed.')
        
    else:
        print('\nPlease enter a valid input.\n')
        main()

def output_dice(dice, index):
    #accepts dice
    #calls roll_die()
    #returns each die in a list
    asdasdasdasd = 9
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
        
    return asdasdasdasd

def roll_die():
    #accepts no arguments
    #rolls an interger from 1-6
    #returns a random interger from 1-6
    dice = random.randint(1,6)
    return dice

def first_roll():
    #accepts no arguments
    #uses roll_die() to generate a list of 12 random intergers
    #returns a list of 12 random intergers
    pass

def count_frequency(dice, index):
    #accepts dice and index
    #finds how often the mode appears
    #returns how often the that target value occurs in the list
    find_mode = stats.mode(index)
    return find_mode

def find_mode(dice, index):
    #accepts dice and index
    #uses count_frequency(dice, number) to determine how often each number occurs
    #returns the mode
    find_mode = count_frequency(dice, index)
    number = find_mode
    return number

def list_unmatched_dice(dice, index, number):
    #accepts dice
    #determines which dice need to be rerolled
    #returns a list of indexes to reroll
    index.sort()
    print(index)
    
    if dice in index != number:
        index.remove(mode)
        
    else:
        print('Thank You For Playing Ezee!')

def reroll_one(dice, index):
    #accepts dice and index
    #calls roll_die() to reroll that index
    #returns a new list with that index rerolled
    pass

def reroll_many(dice):
    #accepts dice
    #calls list_unmatched_dice(dice) and reroll_one(dice, index) to reroll each die != the mode
    #returns a list of rerolled dice
    pass

