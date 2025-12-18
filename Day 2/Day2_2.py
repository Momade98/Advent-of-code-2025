with open("./testinput.txt", "r") as file:
    inputdata = file.read().split(",")

total = 0
for sequence in inputdata:
    sequence = sequence.split("-")
    sequence = list(map(int, sequence))

    # print(range[1] + 1)

    for id in range(sequence[0], sequence[1] + 1):
        counter = 0
        strid = str(id)
        if len(strid) > 1:
            for division in range(2, len(strid)):
                if len(strid) % division == 0:
                    #divide the string in equal parts and compare them (just compare the first part of the string (array) to the rest of the array)