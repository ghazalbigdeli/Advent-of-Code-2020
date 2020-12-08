# Advent of Code 2020 Day 5
# https://adventofcode.com/2020/day/5

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of tickets
    input = []
    for ticket in input_file:
        input.append(ticket)

    # run algorithms
    seat_ids = createSeatIDArray(input)
    print("The highest seat id is:", seat_ids[len(seat_ids) - 1])
    print("My seat id is:", mySeatID(seat_ids))

# part 2
def mySeatID(seat_ids):
    for i in range(len(seat_ids) - 1):
        if (seat_ids[i] + 1 != seat_ids[i + 1]):
            return (seat_ids[i] + 1)

# create sorted list of seat ids
def createSeatIDArray(input):
    seat_ids = []

    for ticket in input:
        seat_ids.append(calculateSeatID(ticket))

    seat_ids.sort()

    return seat_ids

# takes in ticket and returns seatID
    # first 7 characters determine row
    # last three characters determine col
    # seat id = row * 8 + col 
def calculateSeatID(ticket):
    ticket = lettersToBinary(ticket)

    row_bin = int(ticket[0:7])
    col_bin = int(ticket[7:])

    row = binaryToDecimal(row_bin)
    col = binaryToDecimal(col_bin)

    seat_id = row * 8 + col

    return seat_id

# converting letters to binary
# B = 1, F = 0
# R = 1, L = 0
def lettersToBinary(input):
    input = input.replace('B', '1')
    input = input.replace('F', '0')
    input = input.replace('R', '1')
    input = input.replace('L', '0')

    return input

# converting binary number to decimal
def binaryToDecimal(binary):
    decimal = 0

    x = 0
    while (binary != 0):
        next = binary % 10
        binary = int(binary / 10)
        decimal += next * pow(2, x)
        x += 1
    
    return decimal

if __name__ == "__main__":
    main()