# Advent of Code 2020 Day 3 
# https://adventofcode.com/2020/day/3

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # get number of rows
    first = input_file.readline()
    num_rows = len(first) - 1
    input_file.seek(0,0)

    # create array of rows of trees (map)
    input = []
    for row in input_file:
        input.append(row.replace('\n', ''))
    
    # calculate how many columns are needed
    num_rows = len(input)
    num_cols = len(input[0])
    cols_needed = num_rows * 7
    multiplier = int(cols_needed / num_cols) + 1

    # create extended map
    for x in range(len(input)):
        input[x] = input[x] * multiplier

    # part 1
    num_encounters = numEncounters(input, 3, 1)
    print ("Part one - for right 3, down 1, the number of trees encountered are: ", num_encounters)

    # part 2
    product = numEncounters(input, 1, 1) * numEncounters(input, 3, 1) * numEncounters(input, 5, 1) * numEncounters(input, 7, 1) * numEncounters(input, 1, 2)
    print("Part two - product of all encounters:", product)

def numEncounters(input, x_increment, y_increment):
    '''
    Determines the number of trees encountered in a map
    
        Parameters:
            input : map of slope
            x_increment : rightwards movement
            y_increment : downwards movement

        Returns:
            encounters_count : number of trees encountered
    '''
    encounters_count = 0

    # coordinates
    x = 0
    y = 0
    
    while (y < len(input) - 1):
        # calculate new coordinates
        x += x_increment
        y += y_increment

        # check for encounter
        if (input[y][x] == '#'):
            encounters_count += 1

    return encounters_count

if __name__ == "__main__":
    main()