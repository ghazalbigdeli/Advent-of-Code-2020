# Advent of Code 2020 Day 2 
# https://adventofcode.com/2020/day/2

def main():
    # adjust directory accordingly
    inputFile = open("input.txt","r")

    # create array of passwords
    input = []
    for password in inputFile:
        input.append(password)

    # run algorithms
    numValidPartOne(input)
    numValidPartTwo(input)

# part one
# go through each password and check if it passes the policy
def numValidPartOne(input):
    validCount = 0

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
            validCount += 1

    print("Number of valid passwords is: ", validCount)

# part two
# go through each password and check if it passes the policy
def numValidPartTwo(input):
    validCount = 0

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
            validCount += 1

    print("Number of valid passwords is: ", validCount)


if __name__ == "__main__":
    main()