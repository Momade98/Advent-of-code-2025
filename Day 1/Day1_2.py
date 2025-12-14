with open("./input.txt", "r") as file:
    inputdata = file.read().splitlines()


inputdata[0][0]
# print(inputdata)

pointer = 50
tracker = 0
# pointer -= int(inputdata[0][1:])
# print(pointer)
for line in inputdata:
    counter = int(line[1:])
    for x in range(int(line[1:])):
        if pointer == 0:
            tracker += 1

        if line[0] == "L":
            pointer -= 1
            if pointer < 0:
                pointer = 99
        elif line[0] == "R":
            pointer += 1
            if pointer > 99:
                pointer = 0

print(tracker)