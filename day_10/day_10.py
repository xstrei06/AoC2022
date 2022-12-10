f = open("input.txt", "r")
X = 1
cycle = 0
sum = 0
i = 0
for line in f.readlines():
    line = line.split()
    if line[0] == "noop":
        cycle += 1
        if (cycle == 20) or (cycle % 40 == 20):
            sum += cycle * X
        if i in range(X-1, X+2):
            print("#", end="")
        else:
            print(".", end="")
        i += 1
        if i == 40:
            print("")
            i = 0
    elif line[0] == "addx":
        cycle += 1
        if (cycle == 20) or (cycle % 40 == 20):
            sum += cycle * X
        if i in range(X-1, X+2):
            print("#", end="")
        else:
            print(".", end="")
        i += 1
        if i == 40:
            print("")
            i = 0
        cycle += 1
        if (cycle == 20) or (cycle % 40 == 20):
            sum += cycle * X
        if i in range(X-1, X+2):
            print("#", end="")
        else:
            print(".", end="")
        i += 1
        if i == 40:
            print("")
            i = 0
        X += int(line[1])

print("part one: " + str(sum))
f.close()
