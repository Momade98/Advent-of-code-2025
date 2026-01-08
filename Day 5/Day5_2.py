with open("./testinput.txt", "r") as file:
    inputdata = file.read().splitlines()


total = 0
goodIds = []
rangesRaw = []
for line in inputdata:
    if "-" in line:
        rangesRaw.append(line)


for i, range in enumerate(rangesRaw):
    minRangeI = int(range[:range.index("-")])
    maxRangeI = int(range[range.index("-") + 1:])
    for j, nextRange in enumerate(rangesRaw[i+1:]):
        minRangej = int(nextRange[:nextRange.index("-")])
        maxRangej = int(nextRange[nextRange.index("-") + 1:])


for range in rangesRaw:
    counter = int(range[:range.index("-")])
    while counter <= int(range[range.index("-") + 1:]):
        counter += 1
        if counter not in goodIds:
            goodIds.append(counter)


print(len(goodIds))