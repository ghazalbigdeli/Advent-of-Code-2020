# Advent of Code 2020 Day 10
# https://adventofcode.com/2020/day/10

from itertools import combinations

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of jolts
    input = [0]
    for jolt in input_file:
        input.append(int(jolt.strip()))
    
    # sort jolts
    input.sort()
    input.append(input[len(input) - 1] + 3)
    print("jolts:", input)

    # part one
    print("Product for part one:", productOfDifferences(input))

    # part two
    print("Number of arrangements in part two:",countRearrangements(input))

# part one - returns product between num of 1 jolt differences and num of 3 jolt differences 
def productOfDifferences(input):
    diff = calculateDiff(input)
    return diff.count(1) * diff.count(3)

# returns list of differences between the elements of the given list
def calculateDiff(input):
    diff = []
    for i in range(len(input) - 1):
        diff.append(input[i + 1] - input[i])
    return diff

# part two 
# split the groups into subsequences of differences of 1
# get the number of valid arrangements in those subsequences from numArrangements(sub)
# multiply the num of arrangements of each subsequence to get the total num of rearrangements
def countRearrangements(input):
    diff = calculateDiff(input) 
    prev = 0
    count = 1

    for i in range(len(diff)):
        if (diff[i] == 3):
            sub = input[prev : i + 1]
            prev = i + 1
            count *= numArrangements(sub)

    return count

# calculates the number of valid arrangements of a subsequence
def numArrangements(sub):
    if(len(sub) == 1):
        return 1
    
    count = 0
    for i in range(2, len(sub) + 1):
        comb = combinations(sub, i)
        for j in comb:
            diff = calculateDiff(j)
            if (j[0] == sub[0] and j[-1] == sub[-1] and (all(x <= 3 for x in diff))):
                count += 1
    
    return count

if __name__ == "__main__":
    main()