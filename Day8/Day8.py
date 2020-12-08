# Advent of Code 2020 Day 8
# https://adventofcode.com/2020/day/8

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of group answers
    input = []
    for instruction in input_file:
        input.append(instruction.strip())

    # run algorithms
    executeInstructions(input)
    print("Accumulator value in part one:", executeInstructions(input)[1])
    print("Accumulator value in part two:", fixLoop(input))

# run instructions until an infinite loop is meant (instr run for second time)
# return value of accumulator just before that
def executeInstructions(input):
    accumulator = 0
    visited = [False] * len(input)
    fixed = False

    i = 0
    while (i < len(input) and visited[i] == False):
        instruction = input[i][0:3]
        value = int(input[i][4:])
        visited[i] = True

        if (instruction == 'acc'):
            accumulator += value
            i += 1
        elif (instruction =='jmp'):
            i += value
        elif (instruction == 'nop'):
            i += 1

        if (i >= len(input)):
            fixed = True
        else:
            if(visited[i] == True):
                fixed = False
    
    return fixed, accumulator

# fix the instruction
def fixLoop(input):
    fixed = False

    for i in range(len(input)):
        original = input[i]
        instruction = input[i][0:3]
        value = input[i][4:]

        if (instruction == 'jmp'):
            input[i] = 'nop' + ' ' + value
            fixed, accumulator = executeInstructions(input)
            if (fixed):
                print("fixed!")
                return accumulator
            else:
                input[i] = original

        elif (instruction == 'nop'):
            input[i] = 'jmp' + ' ' + value
            fixed, accumulator = executeInstructions(input)
            if (fixed):
                print("fixed!")
                return accumulator
            else:
                input[i] = original
    
    return -1
              
if __name__ == "__main__":
    main()