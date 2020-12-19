# Advent of Code 2020 Day 16
# https://adventofcode.com/2020/day/16

import itertools

# global variables
rules = {}

def main():
    # adjust directory accordingly
    inputFile = open("input.txt","r")

    # grab info
    # create rule dict that contains rule[name] = [min, max, min, max]
    for rule in inputFile:
        ranges = []
        if (rule == '\n'):
            break
        name = rule[0: rule.index(':')]
        rule_split = rule[rule.index(':') + 1:].strip().split(' ')
        i = 0
        while (i <= 2):
            j = rule_split[i].index('-')
            ranges.append(int(rule_split[i][:j]))
            ranges.append(int(rule_split[i][j + 1:]))
            i += 2
        rules[name] = ranges
    inputFile.readline()

    # grab my ticket
    my_ticket = inputFile.readline().strip()
    inputFile.readline()
    inputFile.readline()

    # grab nearby tickets
    nearby_tickets = []
    for ticket in inputFile:
        nearby_tickets.append(ticket.strip())

    # part one
    error_rate, valid_tickets = scanningErrorRate(nearby_tickets)
    print("The error rate in part one is:", error_rate)

    # part two
    # make valid tickets into 2d array (access different columns easier)
    for i in range(len(valid_tickets)):
        valid_tickets[i] = valid_tickets[i].split(',')
    #print("valid tickets are now:", valid_tickets)
    print("The product in part two is:", findOrder(valid_tickets, my_ticket))

# part one
# checks if a value is in a vlid range of any of the rules
def checkValid(num):
    for key, value in rules.items():
        ranges = value
        if (ranges[0] <= num <= ranges[1] or ranges[2] <= num <= ranges[3]):
            return True

    return False

# sum all the invalid values of the nearby tickets
# return list of remaining valid tickets
def scanningErrorRate(nearby_tickets):
    error_rate = 0
    valid_tickets = []

    for ticket in nearby_tickets:
        valid = True
        values = ticket.split(',')
        for num in values:
            if (not checkValid(int(num))):
                error_rate += int(num)
                valid = False
                break
        if(valid):
            valid_tickets.append(ticket)

    return error_rate, valid_tickets

# part two
# checks if a num is valid for a specific field
def checkValidField(num, field):
    ranges = rules[field]
    if (ranges[0] <= num <= ranges[1] or ranges[2] <= num <= ranges[3]):
        return True
    
    return False
    
# each field can only have a unique number of valid columns (ex. 1, 2, 3, 4, etc.)
# find the unique number of columns each field can go into
# go through those in order of ascending, finding the remaining column they're assigned to
def findOrder(valid_tickets, my_ticket):
    # dict in the format of dict[num of valid colummns] = 'class'
    valid_columns = {}
    num_columns = len(valid_tickets[0])

    for field, value in rules.items():
        num_valid = 0 # number of columns that the field is valid for
        # go through each column
        for i in range(num_columns):
            valid = True
            # go through each ticket
            for j in range(len(valid_tickets)):
                if(not checkValidField(int(valid_tickets[j][i]), field)):
                    valid = False
            # increment valid columns number
            if (valid):
                num_valid += 1
            
        valid_columns[num_valid] = field

    columns_left = [i for i in range(num_columns)]
    final_columns = {}
    # go in order starting from the fields with the last num of valid columns
    for i in range(1, len(valid_columns) + 1):
        field = valid_columns[i]
        # check which column it is valid for (should only be one) in remaining cols
        for j in columns_left:
            valid = True
            # go through each ticket
            for k in range(len(valid_tickets)):
                if (not checkValidField(int(valid_tickets[k][j]), field)):
                    valid = False 
            # if it's valid, we found the one
            if(valid):
                final_columns[field] = j
                columns_left.remove(j)
                break

    my_ticket = my_ticket.split(',')
    product = (int(my_ticket[final_columns['departure location']]) * 
            int(my_ticket[final_columns['departure station']]) *
            int(my_ticket[final_columns['departure platform']]) *
            int(my_ticket[final_columns['departure track']]) *
            int(my_ticket[final_columns['departure date']]) *
            int(my_ticket[final_columns['departure time']]))
    
    return product

if __name__ == "__main__":
    main()