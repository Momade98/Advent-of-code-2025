with open("./input.txt", "r") as file:
    inputdata = file.read().splitlines()


total = 0

rangesRaw = []
alreadyUsed = []
ids = []
for line in inputdata:
    if "-" in line:
        rangesRaw.append(line)
    elif len(line) > 0:
        ids.append(line)

separator = ""
for range in rangesRaw:
    separator = range.index("-")

for id in ids:
    for range in rangesRaw:
        if int(id) >= int(range[:range.index("-")]) and int(id) <= int(range[range.index("-") + 1:]) and id not in alreadyUsed:
            total += 1
            alreadyUsed.append(id)
            continue


print(total)