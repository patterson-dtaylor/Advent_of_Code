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
new_total = 0
add = True

while add:
    total = 0
    for n in depths[:3]:
        total += n

    if total > new_total:
        counter += 1
    
    new_total = total

    if not depths:
        add = False
    else:
        depths.pop(0)

print(counter - 1)
