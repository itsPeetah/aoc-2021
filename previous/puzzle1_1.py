with open("puzzle1.txt") as f:
    counter = 0
    firstLine = True
    previousVal = -1
    for line in f:
        val = float(line.strip())
        if not firstLine and val > previousVal: 
            counter+=1
        firstLine = False
        previousVal = val
    print(f"I counted {counter} measurements larger than the previous one.")