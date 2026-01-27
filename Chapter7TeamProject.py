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
    dice = []
    for _ in range(12):
        dice.append(roll_die())
    return dice

def count_frequency(dice, index):
    #accepts dice and index
    #finds how often the mode appears
    #returns how often the that target value occurs in the list
    find_mode = stats.mode(index)
    return find_mode

def find_mode(dice):
    # accepts a list of dice
    # finds which number appears the most
    # returns the mode

    mode = dice[0]
    highest_count = 0

    for number in range(1, 7):
        count = count_frequency(dice, number)
        if count > highest_count:
            highest_count = count
            mode = number

    return mode

def list_unmatched_dice(dice):
    # accepts a list of dice
    # finds which dice are not equal to the mode
    # returns a list of indexes to reroll

    mode = find_mode(dice)
    indexes = []

    for i in range(len(dice)):
        if dice[i] != mode:
            indexes.append(i)

    return indexes

def reroll_one(dice, index):
    # accepts a list of dice and an index
    # rerolls the die at that index
    # returns the updated list

    dice[index] = roll_die()
    return dice

def reroll_many(dice):
    # accepts a list of dice
    # rerolls all dice that are not the mode
    # returns the final list

    rolls = 1

    while True:
        output_dice(dice)

        unmatched = list_unmatched_dice(dice)

        if len(unmatched) == 0:
            break

        for index in unmatched:
            dice = reroll_one(dice, index)

        rolls += 1

    return dice, rolls
   
