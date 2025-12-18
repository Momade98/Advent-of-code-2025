with open("./input.txt", "r") as file:
    inputdata = file.read().split(",")
total = 0
for sequence in inputdata:
    sequence = sequence.split("-")
    sequence = list(map(int, sequence))

    for id in range(sequence[0], sequence[1] + 1):
        strid = str(id)
        if len(strid) % 2 == 0:
            if strid[:len(strid) // 2] == strid[len(strid) // 2:]:
                total += int(strid)

print(total)