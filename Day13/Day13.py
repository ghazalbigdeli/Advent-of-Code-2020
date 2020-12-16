# Advent of Code 2020 Day 13
# https://adventofcode.com/2020/day/13

import math
from functools import reduce

def main():
    # adjust directory accordingly
    inputFile = open("input.txt","r")

    # create array of numbers
    # input = []
    #for instruction in inputFile:
    #    input.append(instruction.strip())
    
    earliest_timestamp = int(inputFile.readline().strip())
    busses = inputFile.readline().strip()
    print("earliest timestamp:", earliest_timestamp)

    # part one
    print("bus ID times waiting time in part one:", earliestBus(earliest_timestamp, busses))

    # part two
    print(earliestOffsetTime(busses))

def earliestBus(earliest_timestamp, busses):
    busses = busses.replace('x,','').split(',')
    dict_busses = {}

    for i in range(len(busses)):
        busses[i] = int(busses[i])
        dict_busses[busses[i]] = -1

    for bus in busses:
        dict_busses[bus] = bus - earliest_timestamp % bus
   
    min_bus = min(dict_busses, key=dict_busses.get)

    return dict_busses[min_bus] * min_bus

# incomplete
def earliestOffsetTime(busses):
    busses = busses.replace('x','0').split(',')
    print(busses)
    for i in range(len(busses)):
        busses[i] = int(busses[i])


if __name__ == "__main__":
    main()
