def fileRead(file):
    input = []
    with open(file, "r", newline=None) as f:
        for line in f:
            line = line.replace("\n", "")
            # line = int(line)
            input.append(line)
    return input

directions = fileRead("input.txt")
horizontal = []
horizontal_total = 0
aim = 0
depth = 0

for direction in directions:
    if "forward" in direction:
        forward = int(direction.replace("forward ", ""))
        horizontal.append(forward)
        depth += (aim * forward)
    elif "down" in direction:
        down = int(direction.replace("down ", ""))
        aim += down
    elif "up" in direction:
        up = int(direction.replace("up ", "-"))
        aim += up

for i in horizontal:
    horizontal_total += i

print(horizontal_total * depth)

