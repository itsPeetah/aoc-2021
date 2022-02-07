import numpy as np

with open("puzzle4.txt") as file:
    nums = [int(x) for x in file.readline().split(',')]
    lines = [[int(x) for x in line.strip().split()] for index,line in enumerate(file.readlines()) if index % 6 != 0]

    boards = []
    for i in range(0, len(lines), 5):
        b = np.array(lines[i:i+5])
        boards.append(b)
    
    found = False
    done = False
    remaining = [x for x in range(len(boards))]
    for num in nums:
        # print("Calling number: ", num)
        for b in range(len(boards)):
            if b not in remaining: continue

            boards[b] = np.where(boards[b] == num, -1, boards[b])
            found = np.isin(-5, [boards[b].sum(0), boards[b].sum(1)])
            done = found and len(remaining) == 1
            if found:
                remaining.remove(b)
                if len(remaining) < 1: break
        if done: break
    
    print(boards[b])

    print("Lucky board:", b)
    board = np.where(boards[b] < 0, 0, boards[b])
    sum = board.sum(0).sum(0).item(0)
    print("The sum is:", sum)
    print("The number is:", num)
    print("Total score: ", sum * num)
    

import numpy as np
n, *b = open(0)                            # read input from stdin
b = np.loadtxt(b, int).reshape(-1,5,5)     # load boards into 3D array

for n in map(int, n.split(',')):           # loop over drawn numbers
    b[b == n] = -1                         # mark current number as -1
    m = (b == -1)                          # get all marked numbers
    win = (m.all(1) | m.all(2)).any(1)     # check for win condition
    if win.any():
        print((b * ~m)[win].sum() * n)     # print winning score
        b = b[~win]                        # remove winning board