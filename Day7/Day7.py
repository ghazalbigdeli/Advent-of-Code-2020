# Advent of Code 2020 Day 7
# https://adventofcode.com/2020/day/7

# global variables
seen = set()
num_bags = 0

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of group rules
    input = []
    for rule in input_file:
        input.append(rule.strip())
    
    # create dictionary of rules
    rule_dict = createDict(input)

    # part one
    numColoursOne('shiny gold', rule_dict)
    print("part one:", len(seen), "bags")

    # part two
    numColoursTwo('shiny gold', rule_dict)
    print("part two:", num_bags, "bags")

# part one
def numColoursOne(colour, rule_dict):
    for key in rule_dict:
        for value in rule_dict[key]:
            if (colour in value):
                seen.add(key)
                numColoursOne(key, rule_dict)
                break

    return

# part two
def numColoursTwo(colour, rule_dict):
    global num_bags
    bags = rule_dict[colour]

    for bag in bags:
        if (bag == 'None'):
            return 0
        else:
            num_bags += int(bag[0]) 
            for i in range(int(bag[0])):
                numColoursTwo(bag[2:], rule_dict)
    
    return

# create dictionary of rules
def createDict(input):
    rule_dict = {}

    for rule in input:
        rule_split = rule.split(' ')
        outer = rule_split[0] + ' ' + rule_split[1]
        
        inner = []
        i = 4

        while i < len(rule_split):
            if (rule_split[i] == 'no'):
                inner.append('None')
            else:
                inner.append(rule_split[i] + ' ' + rule_split[i + 1] + ' ' + rule_split[i + 2])
            i += 4
            
        rule_dict[outer] = inner
    
    return rule_dict

if __name__ == "__main__":
    main()