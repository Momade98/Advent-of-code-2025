with open("./input.txt", "r") as file:
    inputdata = file.read().splitlines()


total = 0
for bank in inputdata:
    biggest = 0
    for x, battery in enumerate(bank):
        for y, secondBattery in enumerate(bank):
            if y > x:
                if int(bank[x] + bank[y]) > biggest:
                    biggest = int(bank[x] + bank[y])
    total += biggest

print(total)