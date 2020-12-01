# main function
def main():
    inputFile = open("C:\\Users\ghaza\Desktop\Advent of Code\Day1\input.txt","r")

    input = []

    for number in inputFile:
        input.append(int(number))

    bruteForceThree(input)
    threeSum(input)

# brute force method for two numbers
def bruteForceTwo(input):
    for x in range(0, len(input)):
        for y in range(x+1, len(input)):
            if (input[x] + input[y] == 2020):
                print("The numbers are: ", input[x], "and ", input[y])
                print("Their product is ", input[x] * input[y])
                return

# brute force method for three numbers
def bruteForceThree(input):
    for x in range(0, len(input)):
        for y in range(x+1, len(input)):
            for z in range(y+1, len(input)):
                if (input[x] + input[y] + input[z] == 2020):
                    print("The numbers are: ", input[x], "and ", input[y], "and ", input[z])
                    print("Their product is ", input[x] * input[y] * input[z])
                    return

# method for two numbers
# uses the two-pointer technique
def twoSum(input):
    # sort the array
    input.sort()
    
    # get the two pointers
    left = 0
    right = len(input) - 1

    # loop to find the sum, adjust accordingly each time
    while (left < right):
        if (input[left] + input[right] == 2020):
            print("The numbers are: ", input[left], "and ", input[right])
            print("Their product is ", input[left] * input[right])   
            return
        elif (input[left] + input[right] > 2020):
            right -= 1
        elif (input[left] + input[right] < 2020):
            left += 1

# method for three numbers
# expand on the two-pointer technique by fixing one of the numbers and searching for the other two
def threeSum(input):
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
                print("Their product is ", input[x] * input[l] * input[r])
                return
            elif (input[x] + input[l] + input[r] > 2020):
                r -= 1
            elif (input[x] + input[l] + input[r] < 2020):
                l += 1


# line that actually starts the code
if __name__ == "__main__":
    main()