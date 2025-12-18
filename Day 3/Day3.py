with open("./testinput.txt", "r") as file:
    inputdata = file.read().splitlines()


total = 0
for bank in inputdata:
    str_totalvoltage = ""
    biggest = [0 , "index"]
    for i, strbattery in enumerate(bank):
        battery = int(strbattery)
        if battery > biggest[0]:
            biggest[0] = battery
            biggest[1] = i
    second_battery = battery.pop(biggest[1])
    for i, strbattery in enumerate(second_battery):
        battery = int(strbattery)
        if battery > biggest[0]:
            biggest[0] = battery
            biggest[1] = i
