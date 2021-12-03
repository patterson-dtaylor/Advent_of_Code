def fileRead(file):
    input = []
    with open(file, "r", newline=None) as f:
        for line in f:
            line = line.replace("\n", "")
            line = int(line)
            input.append(line)
    return input

depths = fileRead("input.txt")
counter = 0
new_depth = 0

for depth in depths:
    if depth > new_depth:
        counter += 1
    
    new_depth = depth

total_increases = counter -1

print(total_increases)

