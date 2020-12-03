# Advent of Code 2020 Day 2 
# https://adventofcode.com/2020/day/2

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of passwords
    input = []
    for password in input_file:
        input.append(password)

    # run algorithms
    print("Part one - number of valid passwords is:", numValidPartOne(input))
    print("Part two - number of valid passwrods is:", numValidPartTwo(input))

# part one
def numValidPartOne(input):
    '''
    Determines the number of valid passwords based on the policy
    (must contain the specified letter within the min-max range)

        Parameters:
            input : list of passwords and their policy

        Returns: 
            valid_count : number of valid passwords

    '''
    valid_count = 0

    for line in input:
        # split input line and range line
        chunks = line.split(' ')
        min_max = chunks[0].split('-')

        # grab info 
        min = int(min_max[0])
        max = int(min_max[1])
        letter = chunks[1][0]
        password = chunks[2]

        # get occurences of letter
        count = password.count(letter)

        # if the count is within the correct range, increment the count
        if (count >= min and count <= max):
            valid_count += 1

    return valid_count

# part two
def numValidPartTwo(input):
    '''
    Determines the number of valid passwords based on the policy
    (specificed letter must appear at only one of the given indices)

        Parameters:
            input : list of passwords and their policy
        
        Returns:
            valid_count : number of valid passwords

    '''
    valid_count = 0

    for line in input:
        # split input line and position line
        chunks = line.split(' ')
        positions = chunks[0].split('-')

        # grab info
        pos1 = int(positions[0]) - 1
        pos2 = int(positions[1]) - 1
        letter = chunks[1][0]
        password = chunks[2]

        # if the letter appears exclusively in one of the valid positions, increment the count
        if (bool(password[pos1] == letter) ^ bool(password[pos2] == letter)):
            valid_count += 1

    return valid_count

if __name__ == "__main__":
    main()