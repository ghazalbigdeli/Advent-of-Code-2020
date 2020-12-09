# Advent of Code 2020 Day 9
# https://adventofcode.com/2020/day/9

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of group answers
    input = []
    for number in input_file:
        input.append(int(number.strip()))

    # run algorithms
    invalid_num = traverseOne(input)
    print("Invalid number:", invalid_num )
    print("Encryption weakness:", contiguousSet(invalid_num, input))

# traverse through list of numbers
def traverseOne(input):
    for i in range(25, len(input)):
        previous = input[i-25:i]
        if (not checkIfSum(input[i], previous)):
            return input[i]
    
    return -1

# checks if the number is a sum of its previous 25 numbers 
def checkIfSum(num, previous):
    for i in range(len(previous) - 1):
        for j in range(i + 1, len(previous)):
            if (previous[i] + previous[j] == num):
                return True
    
    return False

# looks for contigous set that adds up to the invalid number from part one
def contiguousSet(invalid_num, input):
    cont_set = []
    cont_sum = sum(cont_set)

    i = 0
    while (i < len(input)):
        if (input[i] == invalid_num):
            continue
        cont_sum = sum(cont_set)

        if (cont_sum == invalid_num):
            break
        elif (cont_sum > invalid_num):
            cont_set.pop(0)
        elif (cont_sum < invalid_num):
            cont_set.append(input[i])
            i += 1

    # return encryption weakness
    cont_set.sort()
    return cont_set[0] + cont_set[len(cont_set) - 1]    
              
if __name__ == "__main__":
    main()