f = open("input.txt", "r")
count = 0
i = 0
string = f.readline()
while True:
    string2 = string[i: i + 4]
    for char in string2:
        if string2.count(char) > 1:
            break
        else:
            count += 1
    if count == 4:
        print("part one: " + str(i + 4))
        break
    else:
        count = 0
    i += 1

while True:
    string2 = string[i: i + 14]
    for char in string2:
        if string2.count(char) > 1:
            break
        else:
            count += 1
    if count == 14:
        print("part two: " + str(i + 14))
        break
    else:
        count = 0
    i += 1
f.close()
