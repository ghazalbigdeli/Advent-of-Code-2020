# Advent of Code 2020 Day 15
# https://adventofcode.com/2020/day/15

def main():
    # adjust directory accordingly
    inputFile = open("input.txt","r")
    numbers = inputFile.readline().strip().split(',')

    # part one
    print("The 2020th number for part one is:", numberSpoken(numbers, 2020))
    # part two
    print("The 30000000th number for part two is:", numberSpoken(numbers, 30000000))

def numberSpoken(starting_numbers, final_turn):
    # initialize the dict with the starting numbers
    # dict format: key is the number, value is the last two turns that it was used ex. [-1,5] -1 meaning turn 5 was its first time
    numbers = {}
    turn = 1
    for num in starting_numbers:
        numbers[int(num)] = [-1, turn]
        turn += 1

    prev_num = int(starting_numbers[-1])

    while (turn <= final_turn):
        # check if it's the first time
        if (numbers[prev_num][0] == -1):
            prev_num = 0
            numbers[0] = [numbers[0][1], turn]
        else:
            new_num = numbers[prev_num][1] - numbers[prev_num][0]
            if (new_num in numbers.keys()):
                numbers[new_num] = [numbers[new_num][1], turn]
            else:
                numbers[new_num] = [-1, turn]
            prev_num = new_num
            
        turn += 1

    return prev_num

if __name__ == "__main__":
    main()
