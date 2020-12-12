# Advent of Code 2020 Day 11
# https://adventofcode.com/2020/day/11

from array import *
import copy

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of seats
    input = []
    for seats in input_file:
        #input.append(seats.strip())
        input.append(list(seats.strip()))

    # create array of directions
    global directions
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    new_seats = [None] * len(input)
    for i in range(len(new_seats)):
        new_seats[i] = [None] * len(input[0])

    # part one
    new_seats, changed = traverseOne(input)
    while (changed == True):
        new_seats, changed = traverseOne(new_seats)
    
    count = 0
    for i in new_seats:
        count += i.count('#')
    
    print("Number of occupied seats in part one:", count)

    # part two
    new_seats, changed = traverseTwo(input)
    while (changed == True):
        new_seats, changed = traverseTwo(new_seats)
    
    count = 0
    for i in new_seats:
        count += i.count('#')
    
    print("Number of occupied seats in part two:", count)
    
# traverse and apply changes accordingly (applied simultaneously)
# if seat is empty (L), and there are no occupied seats adjacent (8) to it, seat becomes occupied
# if seat is occupied(#), and four or more seats adjacent are occupied, it becomes empty
def traverseOne(input):
    changed = False
    # create copy array for storing new seat info
    new_seats = copy.deepcopy(input)

    # go through each seat and apply changes accordingly (save in new_seats)
    for i in range(len(input)):
        for j in range(len(input[i])):
            seat = input[i][j]
            num_occupied = checkNumOccupiedOne(i, j, input)

            if (seat == 'L' and num_occupied == 0):
                new_seats[i][j] = '#'
                changed = True
            elif (seat == '#' and num_occupied >= 4):
                new_seats[i][j] = 'L'
                changed = True
            else:
                new_seats[i][j] = seat

    # return whether the seating was changed, so you know when to stop
    return new_seats, changed

# checks to see if any of the adjacent seats are occupied
# return true if occupied
def checkNumOccupiedOne(x, y, input):
    occupied = 0
    for direction in directions:
        i = direction[0]
        j = direction[1]
        if (0 <= (x + i) < len(input) and 0 <= (y + j) < len(input[0])):
            if (input[x + i][y + j] == '#'):
                occupied += 1      
    
    return occupied

# PART TWO -- same functions adjusted for part two criteria

# traverse and apply changes accordingly
# same rules as before, except an adjacent seat is the first visible seat in that direction
# also occupied threshold is now <= 5 instead of 4
def traverseTwo(input):
    changed = False
    # create copy array for storing new seat info
    new_seats = copy.deepcopy(input)

    for i in range(len(input)):
        for j in range(len(input[i])):
            seat = input[i][j]
            num_occupied = checkNumOccupiedTwo(i, j, input)
            if (seat == 'L' and num_occupied == 0):
                new_seats[i][j] = '#'
                changed = True
            elif (seat == '#' and num_occupied >= 5):
                new_seats[i][j] = 'L'
                changed = True
            else:
                new_seats[i][j] = seat

    return new_seats, changed

def checkNumOccupiedTwo(x, y, input):
    occupied = 0

    for direction in directions:
        i = direction[0] # x increment
        j = direction[1] # y increment
        new_x = x + i
        new_y = y + j
        
        while(0 <= new_x < len(input) and 0 <= new_y < len(input[0])):
            # break once a seat is found
            # since you can't see anything past empty/occupied seat
            if (input[new_x][new_y] == '#'):
                occupied += 1
                break
            if (input[new_x][new_y] == 'L'):
                break 
            
            # increment in the same direction
            new_x += i
            new_y += j
    
    return occupied

if __name__ == "__main__":
    main()