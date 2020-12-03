# Advent of Code 2020 Day 1 
# https://adventofcode.com/2020/day/1

def main():
    # adjust directory accordingly
    inputFile = open("input.txt","r")

    # create array of numbers
    input = []
    for number in inputFile:
        input.append(int(number))
    
    # run algorithms
    print("Part one - the product is", twoSum(input))
    print("Part two - the product is", threeSum(input))

# part one
def twoSum(input):
    '''
    Determines and prints the product of the two numbers that add up to 2020
    Using two-pointer technique

        Parameters:
            input : list of numbers
        
        Returns:
            product : product of the two numbers
    '''
    # sort the array
    input.sort()
    
    # get the two pointers
    l = 0
    r = len(input) - 1

    # loop to find the sum, adjust accordingly each time
    while (l < r):
        if (input[l] + input[r] == 2020):
            print("The numbers are: ", input[l], "and ", input[r])
            product = input[l] * input[r]   
            return product
        elif (input[l] + input[r] > 2020):
            r -= 1
        elif (input[l] + input[r] < 2020):
            l += 1

# method for three numbers
# expand on the two-pointer technique by fixing one of the numbers and searching for the other two
def threeSum(input):
    '''
    Determines and prints the product of the three numbers that add up to 2020
    Expands on two-pointer technique by fixing one of the numbers

        Parameters:
            input : list of numbers
        
        Returns:
            product : product of the three numbers
    '''
    # sort the array
    input.sort()

    # fix the first number
    for x in range(len(input)):
        l = 0
        r = len(input) - 1

        # loop to find the sum, adjust accordingly each time
        while (l < r):
            if (input[x] + input[l] + input[r] == 2020):
                print("The numbers are: ", input[x], "and ", input[l], "and ", input[r])
                product = input[x] * input[l] * input[r]
                return product
            elif (input[x] + input[l] + input[r] > 2020):
                r -= 1
            elif (input[x] + input[l] + input[r] < 2020):
                l += 1

if __name__ == "__main__":
    main()