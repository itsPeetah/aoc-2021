from os import O_TRUNC


with open("puzzle3.txt") as file:
    
    # Found from part one
    gamma = "001110101101"
    epsilon = "110001010010"
    
    oxiNumbers = []
    co2Numbers = []
    
    for line in file:
        oxiNumbers.append(line.strip())
        co2Numbers.append(line.strip())

    bit = 0
    zeros, ones = [], []
    while len(oxiNumbers) > 1:
        
        zeros = [x for x in oxiNumbers if x[bit] == "0"]
        ones = [x for x in oxiNumbers if x[bit] == "1"]

        oxiNumbers = zeros if len(zeros) > len(ones) else ones

        bit+=1
    bit = 0
    while len(co2Numbers) > 1:
        
        zeros = [x for x in co2Numbers if x[bit] == "0"]
        ones = [x for x in co2Numbers if x[bit] == "1"]

        co2Numbers = ones if len(ones) < len(zeros) else zeros

        bit+=1

    oxigenGeneratorRating = oxiNumbers.pop()
    co2ScrubberRating = co2Numbers.pop()

    print(f"Oxigen generator rating: {int(oxigenGeneratorRating, 2)} ({oxigenGeneratorRating})")
    print(f"CO2 scrubber rating: {int(co2ScrubberRating, 2)} ({co2ScrubberRating})")
    print(f"Life support rating: {int(oxigenGeneratorRating,2) * int(co2ScrubberRating,2)}")
            

