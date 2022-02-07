with open("puzzle2.txt") as file:
    x, y, aim, f = 0, 0, 0, 0
    for line in file:
        split = line.split()
        f = int(split[1])
        if split[0] == "forward":
            x += f
            y += f * aim
        else:
            aim += f if split[0] == "down" else -f
    
    print(f"I am now ad x: {x}, y: {y}. x * y = {x * y}")