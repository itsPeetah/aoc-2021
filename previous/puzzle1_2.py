measurements = []
with open("puzzle1.txt") as file:
    measurements = [float(line[:-1]) for line in file]

counter = 0
previousWindow = -1
firstWindow = False
for i in range(len(measurements) - 2):
    window = measurements[i] + measurements[i+1] + measurements[i+2]
    if not firstWindow and window > previousWindow:
        counter += 1
    firstWindow = False
    previousWindow = window

print(f"I counted {counter} 3-measurement windows the sum of which was larger than the previous one.")