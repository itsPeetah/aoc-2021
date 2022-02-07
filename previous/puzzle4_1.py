import numpy as np

with open("puzzle4.txt") as file:
    nums = [int(x) for x in file.readline().split(',')]
    lines = [[int(x) for x in line.strip().split()] for index,line in enumerate(file.readlines()) if index % 6 != 0]

    boards = []
    for i in range(0, len(lines), 5):
        b = np.array(lines[i:i+5])
        boards.append(b)
    
    found = False
    for num in nums:
        # print("Calling number: ", num)
        for b in range(len(boards)):
            boards[b] = np.where(boards[b] == num, -1, boards[b])
            found = np.isin(-5, [boards[b].sum(0), boards[b].sum(1)])
            if found: break
        if found: break

    print("Lucky board:", b)
    board = np.where(boards[b] < 0, 0, boards[b])
    sum = board.sum(0).sum(0).item(0)
    print("The sum is:", sum)
    print("The number is:", num)
    print("Total score: ", sum * num)
        