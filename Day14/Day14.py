# Advent of Code 2020 Day 14
# https://adventofcode.com/2020/day/14

import itertools

def main():
    # adjust directory accordingly
    inputFile = open("input.txt","r")

    # create array of numbers
    input = []
    for instruction in inputFile:
        input.append(instruction.strip())

    # part one
    print("Sum in part one:", initializationProgram(input))
    # part two
    print("Sum in part two:", addressDecoder(input))

# part one - run all masking
def initializationProgram(input):
    # initialize memory
    memory = {}
    mask = 0

    for instruction in input:
        if (instruction.count('mask') == 1): # new mask
            mask = instruction[7:]
            off_mask = int(mask.replace('X','1'), base=2) # use AND - applies the 0's from the mask ("bits masked off" = bits masked to 0)
            on_mask = int(mask.replace('X','0'), base=2) # use OR - applies the 1's from the mask ("bits masked on" = bits masked to 1) 
            continue

        address = int(instruction[4:(instruction.index(']'))])
        dec_value = int(instruction[instruction.index('=') + 2:])

        memory[address] = (dec_value | on_mask) & off_mask
    
    sum = 0
    for key, value in memory.items():
        sum += value

    return sum

# part two
# If the bitmask bit is 0, the corresponding memory address bit is unchanged.
# If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
# If the bitmask bit is X, the corresponding memory address bit is floating.
def addressDecoder(input):
    # initalize memory
    memory = {}

    for instruction in input:
        if (instruction.count('mask') == 1): # new mask
            mask = instruction[7:]
            # create on mask to first apply the overwriting of 1
            on_mask = int(''.join(m if m == '1' else '0' for m in mask), base=2)
            # grab indices of the X's
            floating_index = [i - len(mask) for i, a in enumerate(mask) if a == "X"]
            continue # go to next instruction line
        
        dec_value = int(instruction[instruction.index('=') + 2:])
        address = bin(int(instruction[4:(instruction.index(']'))]) | on_mask)

        # convert address to list for ease of changing, fill with 0's
        address = list(str(address[2:]).zfill(36))

        # create list of combinations for the floating variables
        combinations = list(itertools.product([0,1], repeat=len(floating_index)))

        # save the dec value in each new combinaton of addresses
        for combination in combinations:
            new_address = address
            for pos, value in zip(floating_index, combination):
                new_address[pos] = str(value)
            
            new = int("".join(new_address),2)
            memory[new] = dec_value

    # calculate the sum of the values in memory
    sum = 0
    for key, value in memory.items():
        sum += value

    return sum

if __name__ == "__main__":
    main()
