# Advent of Code 2020 Day 12 
# https://adventofcode.com/2020/day/12

def main():
    # adjust directory accordingly
    inputFile = open("input.txt","r")

    # create array of numbers
    input = []
    for instruction in inputFile:
        input.append(instruction.strip())
    
    # part one
    print("Manhattan distance in part one:", runInstructionsOne(input))

    # part two  
    print("Manhattan distance in part two:", runInstructionsTwo(input))

def runInstructionsOne(instructions):
    facing = 'east'
    ship_x = 0
    ship_y = 0

    # list of directions used for rotating
    directions = ['north', 'east', 'south', 'west']

    # apply each instruction
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        # for changing direction
        index = directions.index(facing)
        increment = value // 90

        # adjust accordingly
        if (action == 'F'):
            if (facing == 'east'): ship_x += value
            elif (facing == 'west'): ship_x -= value
            elif (facing == 'north'): ship_y += value
            elif (facing == 'south'): ship_y -= value
        elif (action == 'E'): ship_x += value
        elif (action == 'W'): ship_x -= value
        elif (action == 'N'): ship_y += value
        elif (action == 'S'): ship_y -= value
        elif (action == 'R'):
            if (index + increment > 3):
                increment -= 4
            facing = directions[index + increment]
        elif (action == 'L'):
            facing = directions[index - increment]

    return abs(ship_x) + abs(ship_y)

def runInstructionsTwo(instructions):
    ship_x = 0
    ship_y = 0
    waypoint_x = 10
    waypoint_y = 1

    # apply each instruction
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        # for changing direction
        increment = value // 90

        # adjust accordingly
        if (action == 'F'): # move the ship towards the waypoint [value] number of times
           ship_x += waypoint_x * value
           ship_y += waypoint_y * value
        elif (action == 'E'): waypoint_x += value
        elif (action == 'W'): waypoint_x -= value
        elif (action == 'N'): waypoint_y += value
        elif (action == 'S'): waypoint_y -= value
        elif (action == 'R'):
            for i in range(increment):
                temp = waypoint_x
                waypoint_x = waypoint_y
                waypoint_y = -temp
        elif (action == 'L'):
            for i in range(increment):
                temp = waypoint_x
                waypoint_x = -waypoint_y
                waypoint_y = temp
    
    return abs(ship_x) + abs(ship_y)

if __name__ == "__main__":
    main()
