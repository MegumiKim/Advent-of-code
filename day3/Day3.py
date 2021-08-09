# Part 1: 
# Starting at the top-left corner of your map 
# and following a slope of right 3 and down 1, 
# how many trees would you encounter?

with open('/Users/megumi/Desktop/Python/Advent/day3/input') as file:
    lines = file.read().splitlines()

    tree_counts = 0 
y = 0 #vertical cordinate
x = 0 #horizontal cordinate

while y < len(lines)-1:
    x = (x+3)%(len(lines[0]))
    y += 1  
        
    if lines[y][x] == "#":
        tree_counts +=1

print("Part1:", tree_counts)

# Part 2:
# What do you get if you multiply together the number 
# of trees encountered on each of the listed slopes?

def slopes(right,down):
    tree_counts = 0 
    y = 0 #vertical cordinate
    x = 0 #horizontal cordinate

    while y < len(lines)-1:
        x = (x+right)%(len(lines[0]))
        y += down  

        if lines[y][x] == "#":
            tree_counts +=1
            
    return tree_counts
    
print("Part2:", slopes(1,1)*slopes(3,1)*slopes(5,1)*slopes(7,1)*slopes(1,2))