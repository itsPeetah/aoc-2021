with open("puzzle3.txt") as file:
    lineCounter = 0
    sums = {}
    for line in file:
        for i,digit in enumerate(line[:-1]):
            if i in sums: sums[i] += int(digit)
            else: sums[i] = int(digit)
        lineCounter+=1
    
    gamma = ""
    epsilon = ""
    for k,v in sums.items():
        if v * 2 > lineCounter :
            gamma += "1"
            epsilon += "0"
        elif v * 2 < lineCounter :
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    
    print(f"Gamma rate: {gamma} ({int(gamma, 2)}), Epsilon rate: {epsilon} ({int(epsilon, 2)})")
    print(f"Power consuption: {bin(int(gamma, 2) * int(epsilon, 2))[2:]} ({int(gamma, 2) * int(epsilon, 2)})")