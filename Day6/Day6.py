# Advent of Code 2020 Day 6
# https://adventofcode.com/2020/day/6

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of group answers
    input = []
    group = ''
    for line in input_file:
        if (line == '\n'): # new group
            group = group.strip()
            input.append(group)
            group = ''
        else:
            group += line.replace('\n',' ')
    input.append(group)

    # run algorithms
    print("The sum of the counts in part one is:", sumCountsOne(input))
    print("The sum of the counts in part two is:", sumCountsTwo(input))

# part one
def sumCountsOne(input):
    sum = 0

    for group in input:
        group = group.replace(' ', '')
        sum += len(set(group))
    
    return sum

# part two
def sumCountsTwo(input):
    sum = 0

    for group in input:
        group_split = group.split()

        if (len(group_split) == 1):
            sum += len(group_split[0])
        else:
            common = group_split[0]
            for answers in group_split[1:]:
                common = set(common) & set(answers)
            sum += len(common)
    
    return sum

if __name__ == "__main__":
    main()