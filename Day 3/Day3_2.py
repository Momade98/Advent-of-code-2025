with open("./input.txt", "r") as file:
    inputdata = file.read().splitlines()


total = 0
for bank in inputdata:
    counter = 12
    goodbank = ""
    while counter > 0:
        if len(bank) <= counter:
            goodbank += bank
            break
        else:
            bankNumerical = list(map(int, list(bank[:len(bank) - counter + 1]))) #starting index not good for bank!! NEED CHANGE
            indexMax = bankNumerical.index(max(bankNumerical))

            goodbank += str(max(bankNumerical))
            bank = bank[indexMax + 1:]
            counter -= 1

    total += int(goodbank)

print(total)