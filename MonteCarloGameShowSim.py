'''
Created on Nov 22, 2016

@author: Benjamin Hodgson
'''

import random

def runSim(doors, runs):
    '''
    simulates the probability of choosing the 
    winning door out of integer number of possible 
    doors stored in parameter doors an integer number
    of times stored in parameter number
    '''
    num_won = 0
    num_game = 0
    while True: 
        # print num_game
        if num_game == runs:
            break
        guess_choice = random.choice(range(doors))
        #randomize_doors = []
        winning_door = random.choice(range(doors))
#         for number in range(doors):
#             if number == winning_door:
#                 randomize_doors.append("car")
#             else:
#                 randomize_doors.append("goat")
        remove_door = 0
        # randomize_doors[remove_door] = "EMPTY"
        while True:
            rand_remove_door = random.choice(range(doors))
            if rand_remove_door != winning_door:
                if rand_remove_door != guess_choice:
                    remove_door = rand_remove_door
                    break
        new_choice = 0
        while True:
            rand_new_choice = random.choice(range(doors))
            if rand_new_choice != guess_choice:
                if rand_new_choice != remove_door:
                    new_choice = rand_new_choice
                    break
#         print "Original choice:", guess_choice, randomize_doors[guess_choice]
#         print "Winning door:", winning_door, randomize_doors[winning_door]
#         print "Original door order:", randomize_doors
#         print "Remove door:", remove_door, randomize_doors[remove_door]
#         print "New choice:", new_choice, randomize_doors[new_choice]
        if new_choice == winning_door:
            num_won += 1
        num_game += 1
    percent_won = 0
    if num_won != 0:
        percent_won = float(num_won)/num_game
    print "Number of switches to winning door:", num_won
    print "Number of simulations run:", num_game
    print "Percent won:", percent_won
    
if __name__ == '__main__':
    runSim(3, 50000)