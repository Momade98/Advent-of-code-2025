with open("./input.txt", "r") as file:
    inputdata = file.read().splitlines()


totalGoodOnes = 0
repeat = True

while repeat is True:
    goodOnesCoordinates = []
    for y, line in enumerate(inputdata):
        for x, thing in enumerate(line):
            total = 0
            if thing == "@":
                # up
                if y - 1 >= 0 and x - 1 >= 0 and inputdata[y - 1][x-1] == "@":
                    total += 1
                if y - 1 >= 0 and inputdata[y - 1][x] == "@":
                    total += 1
                if y - 1 >= 0 and x + 1 <= len(line) - 1 and inputdata[y - 1][x+1] == "@":
                    total += 1
                # middle
                if x - 1 >= 0 and inputdata[y][x-1] == "@":
                    total += 1
                if x + 1 <= len(line) - 1 and inputdata[y][x+1] == "@":
                    total += 1
                # down
                if y + 1 <= len(inputdata) - 1 and x - 1 >= 0 and inputdata[y + 1][x-1] == "@":
                    total += 1
                if y + 1 <= len(inputdata) - 1 and inputdata[y + 1][x] == "@":
                    total += 1
                if y + 1 <= len(inputdata) - 1 and x + 1 <= len(line) - 1 and inputdata[y + 1][x+1] == "@":
                    total += 1


                if total < 4:
                    totalGoodOnes += 1
                    goodOnesCoordinates.append((y, x))


    if goodOnesCoordinates:
        for coordinates in goodOnesCoordinates:
            y = coordinates[0]
            x = coordinates[1]
            newY = inputdata[y][:x] + "x" + inputdata[y][x+1:]
            inputdata[y] = newY
    else:
        repeat = False



for line in inputdata:
    print(line)

print(totalGoodOnes)