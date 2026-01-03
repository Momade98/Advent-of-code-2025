with open("./input.txt", "r") as file:
    inputdata = file.read().splitlines()

# print(inputdata)


totalGoodOnes = 0
for y, line in enumerate(inputdata):
    for x, thing in enumerate(line):
        if thing == "@":
            total = 0
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

print(totalGoodOnes)