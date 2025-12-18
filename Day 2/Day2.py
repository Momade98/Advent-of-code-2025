with open("./input.txt", "r") as file:
    inputdata = file.read().split(",")

# print (inputdata)
# print(inputdata[0].split("-"))


# test = 1188511885
# test = str(test)
# if len(test) % 2 == 0:
#     print(test[:len(test) // 2])

total = 0
for sequence in inputdata:
    sequence = sequence.split("-")
    sequence = list(map(int, sequence))

    # print(range[1] + 1)

    for id in range(sequence[0], sequence[1] + 1):
        # print(id)
        strid = str(id)
        if len(strid) % 2 == 0:
            if strid[:len(strid) // 2] == strid[len(strid) // 2:]:
                total += int(strid)

print(total)