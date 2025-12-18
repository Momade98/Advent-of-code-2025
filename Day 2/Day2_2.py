import textwrap

with open("./input.txt", "r") as file:
    inputdata = file.read().split(",")

total = 0
for sequence in inputdata:
    sequence = sequence.split("-")
    sequence = list(map(int, sequence))

    invalid_id = []
    for id in range(sequence[0], sequence[1] + 1):
        strid = str(id)
        if len(strid) > 1:
            for division in range(2, len(strid) + 1):
                if len(strid) % division == 0:
                    idSeparated = textwrap.wrap(strid, len(strid) // division)
                    counter = 0
                    for parOfId in idSeparated:
                        if idSeparated[0] != parOfId:
                            counter += 1
                    if counter == 0 and id not in invalid_id:
                        invalid_id.append(id)
    for id in invalid_id:
        total += id

print(total)         