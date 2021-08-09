# Part 1: Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number of times 
# a given letter must appear for the password to be valid.
# How many passwords are valid according to their policies?

def passwd_dict(string):

    passwd_d = {}   
    item = string.split()

    passwd_d["min"] = int(item[0].split("-")[0])
    passwd_d["max"] = int(item[0].split("-")[1])
    passwd_d["char"] = item[1][0]
    passwd_d["pswd"] = item[2]

    return passwd_d    


def valid_passwd(dic):
    return dic['min'] <= dic['pswd'].count(dic["char"]) <= dic["max"]


def valid_psswd_count(lines):
    count = 0
    
    for line in lines:
        if valid_passwd(line):
            count+=1
    return count


with open("/Users/megumi/Desktop/Python/Advent/day2/input") as file:
    inputs = [passwd_dict(line) for line in file]


print("Part1:", valid_psswd_count(inputs))

# Part 2: Each policy actually describes two positions in the password, 
# where 1 means the first character, 2 means the second character, and so on.

def valid_passwd_2(dic):
    return (dic['pswd'][dic['min']-1]==dic['char']) != (dic['pswd'][dic['max']-1]==dic['char'])


def valid_psswd_count2(lines):
    count = 0
    
    for line in lines:
        if valid_passwd_2(line):
            count+=1
    return count

print("Part2:", valid_psswd_count2(inputs))