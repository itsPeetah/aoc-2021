print("My original solution")
with open("puzzle2.txt") as f:
    x, y = 0, 0
    for line in f:
        split = line.split()
        if split[0] == "forward":
            x += int(split[1])
        else:
            y += int(split[1]) if split[0] == "down" else -int(split[1])
    
    print(f"I am now ad x: {x}, y: {y}. x * y = {x * y}")


print("Trying out the match statement")
#https://www.reddit.com/r/adventofcode/comments/r6zd93/2021_day_2_solutions/hmwbtbe/
with open("puzzle2.txt") as file:
    x, y = 0,0
    for line in file:
        match line.split():
            case 'forward', n:
                x += int(n)
            case 'down', n:
                y += int(n)
            case 'up', n:
                y -= int(n)
    print(f"I am now ad x: {x}, y: {y}. x * y = {x * y}")