with open("./testestinput.txt", "r") as file:
    inputdata = file.read().splitlines()


total = 0
goodIds = []
rangesRaw = []
for line in inputdata:
    if "-" in line:
        rangesRaw.append(line)


counter = 0
repeat = True

while repeat is True:
    for i, range in enumerate(rangesRaw):
        minRangeI = int(range[:range.index("-")])
        maxRangeI = int(range[range.index("-") + 1:])
        for j, nextRange in enumerate(rangesRaw[i+1:]):
            minRangej = int(nextRange[:nextRange.index("-")])
            maxRangej = int(nextRange[nextRange.index("-") + 1:])


            if minRangeI >= minRangej and maxRangeI <= maxRangej:
                rangesRaw.remove(range)
                counter += 1
                repeat = True
            elif minRangej >= minRangeI and maxRangej <= maxRangeI:
                rangesRaw.remove(nextRange)
                counter += 1
                repeat = True
            else:
                repeat = False


print(rangesRaw)
print(counter)