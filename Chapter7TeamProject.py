import random

def main(): #Brody
    #accepts no arguments
    #calls all functions
    #returns nothing
    pass

def output_dice(dice): #Brody
    #accepts dice
    #calls roll_die()
    #returns each die in a list
    pass

def roll_die(): #Brody
    #accepts no arguments
    #rolls an interger from 1-6
    #returns a random interger from 1-6
    pass

def first_roll(): #Brody
    #accepts no arguments
    #uses roll_die() to generate a list of 12 random intergers
    #returns a list of 12 random intergers
    pass

def count_frequency(dice, number): #Brody
    #accepts dice and number
    #finds how often the mode appears
    #returns how often the that target value occurs in the list
    pass

def find_mode(dice): #Oliver
    #accepts dice
    #uses count_frequency(dice, number) to determine how often each number occurs
    #returns the mode
    pass

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

