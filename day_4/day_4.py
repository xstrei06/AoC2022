f = open("input.txt", "r")
first = ""
second = ""
count1 = 0
count2 = 0
added = 0
for line in f.readlines():
    if line == "\n":
        continue
    line = line.strip("\n").split(",")
    first_elf = line[0].split("-")
    second_elf = line[1].split("-")
    if int(first_elf[0]) >= int(second_elf[0]) and int(first_elf[1]) <= int(second_elf[1]):
        count1 += 1
    elif int(second_elf[0]) >= int(first_elf[0]) and int(second_elf[1]) <= int(first_elf[1]):
        count1 += 1
    for i in range(int(first_elf[0]), int(first_elf[1])+1):
        if i == int(second_elf[0]) or i == int(second_elf[1]):
            count2 += 1
            added = 1
            break
    if added == 1:
        added = 0
        continue
    for i in range(int(second_elf[0]), int(second_elf[1])+1):
        if i == int(first_elf[0]) or i == int(first_elf[1]):
            count2 += 1
            break
print("one range in the other: " + str(count1))
print("overlap at all: " + str(count2))
