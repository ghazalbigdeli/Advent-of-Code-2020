# Advent of Code 2020 Day 4 
# https://adventofcode.com/2020/day/4

def main():
    # adjust directory accordingly
    input_file = open("input.txt","r")

    # create array of passports
    input = []
    passport = ''
    for line in input_file:
        if (line == '\n'): # new passport
            passport = passport.strip()
            input.append(passport)
            passport = ''
        else:
            passport += line.replace('\n', ' ')
    input.append(passport)

    # run algorithms
    print("The number of valid passports in part one are", validPassportsOne(input))
    print("The number of valid passports in part two are", validPassportsTwo(input))

def validPassportsOne(input):
    '''
    Determines how many passports are valid (have all 7 necessary info)

        Parameters:
            input : list of passports

        Returns:
            valid_count : number of valid passports
    '''
    valid_count = 0
    
    # go through each passport
    for passport in input:
        info_count = passport.count(':')
        
        if (info_count == 8):
            valid_count += 1
        elif (info_count == 7):
            if (passport.count('cid') == 0):
                valid_count += 1
        
    return valid_count

def validPassportsTwo(input):
    '''
    Determines how many passports are valid based on the given requirements

        Parameters:
            input : list of passports
        
        Returns:
            valid_count : number of valid passports
    '''
    valid_count = 0

    # go through each passport
    for passport in input:
        valid = False

        info_count = passport.count(':')

        # make sure it has all necessary info 
        if (info_count == 8):
            valid = True
        elif (info_count == 7):
            if (passport.count('cid') == 0):
                valid = True
                
        split_passport = passport.split(' ')

        # go through each piece of info to see if it's valid
        for info in split_passport:
            if(not valid):
                break

            info_split = info.split(':')
            field = info_split[0]
            value = info_split[1]

            # birth year
            if (field == 'byr'):
                value = int(value)
                if (not(value >= 1920 and value <= 2002)):
                    valid = False
                    break
            # issue year
            elif (field == 'iyr'):
                value = int(value)
                if (not(value >= 2010 and value <= 2020)):
                    valid = False
                    break
            # expiration year
            elif (field == 'eyr'):
                value = int(value)
                if (not(value >= 2020 and value <= 2030)):
                    valid = False
                    break
            # height
            elif (field == 'hgt'):
                # if cm
                if (value.count('cm') == 1):
                    value = int(value.replace('cm',''))
                    if (not(value >= 150 and value <= 193)):
                        valid = False
                        break
                elif(value.count('in') == 1):
                    value = int(value.replace('in',''))
                    if (not(value >= 59 and value <= 76)):
                        valid = False
                        break
            # hair colour
            elif (field == 'hcl'):
                if(not(value.count('#') == 1) and len(value) == 7):
                    valid = False
                    break

                bad_letters = 'ghijklmnopqrstuvwxyz'
                for char in value:
                    if char in bad_letters:
                        valid = False
                        break
            # eye colour
            elif (field == 'ecl'):
                if (not(value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth')):
                    valid = False
                    break
            # passport id
            elif (field == 'pid'):
                if (not(len(value) == 9)):
                    valid = False
                    break

        if (valid):
            valid_count += 1
        
    return valid_count
        
if __name__ == "__main__":
    main()