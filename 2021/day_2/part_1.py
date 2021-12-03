def fileRead(file):
    input = []
    with open(file, "r", newline=None) as f:
        for line in f:
            line = line.replace("\n", "")
            input.append(line)
    return input

directions = fileRead("input.txt")
horizontal = []
horizontal_total = 0
vertical = []
vertical_total = 0

for direction in directions:
    if "forward" in direction:
        forward = direction.replace("forward ", "")
        horizontal.append(int(forward))
    elif "down" in direction:
        down = direction.replace("down ", "")
        vertical.append(int(down))
    elif "up" in direction:
        up = direction.replace("up ", "-")
        vertical.append(int(up))

for i in horizontal:
    horizontal_total += i

for i in vertical:
    vertical_total += i

print(horizontal_total * vertical_total)


