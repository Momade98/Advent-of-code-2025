with open("./input.txt", "r") as file:
    inputdata = file.read().splitlines()


inputdata[0][0]
# print(inputdata)

pointer = 50
tracker = 0
# pointer -= int(inputdata[0][1:])
# print(pointer)
for line in inputdata:
    if line[0] == "L":
        pointer -= int(line[1:])
    elif line[0] == "R":
        pointer += int(line[1:])

    if (pointer < 0):
        while(True):
            pointer += 100
            if (pointer >= 0):
                break
    elif (pointer > 99):
        while(True):
            pointer -= 100
            if (pointer <= 99):
                break  
    

    if pointer == 0:
        tracker += 1
    
print(tracker)