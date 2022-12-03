f = open("data.txt", 'r')
line = f.readline()
max = 0
elf = 0
top2 = 0
top3 = 0
for line in f.readlines():
    if line == '\n':
        if max < elf:
            top3 = top2
            top2 = max
            max = elf
        elif top2 < elf:
            top3 = top2
            top2 = elf
        elif top3 < elf:
            top3 = elf
        elf = 0
    else:
        elf += int(line)
print("most calories: " + str(max))
print("top three: " + str(max + top2 + top3))
f.close()
