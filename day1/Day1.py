# Part 1: Find the two entries that sum to 2020;
# what do you get if you multiply them together?

with open('./input.txt') as file:
# with open('/Users/megumi/Desktop/Python/Advent/day1/input.txt') as file:
    inputs = [int(line) for line in file]

def expense(report):
    for n in report:
        if 2020-n in report:
            return n*(2020-n)
print(file)        
print("Part1:", expense(inputs))


#Part 2: what is the product of the three entries that sum to 2020?

def expense_2(report):
    for n in report:
        for n2 in report:
            if 2020-n-n2 in report:
                return n*n2*(2020-n-n2)
        
print("Part2:", expense_2(inputs))