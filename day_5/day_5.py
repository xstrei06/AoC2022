f = open("input.txt", "r")
stacks = ["TDWZVP", "LSWVFJD", "ZMLSVTBH",
          "RSJ", "CZBGFMLW", "QWVHZRGB",
          "VJPCBDN", "PTBQ", "HGZRC"]
stacks2 = ["TDWZVP", "LSWVFJD", "ZMLSVTBH",
           "RSJ", "CZBGFMLW", "QWVHZRGB",
           "VJPCBDN", "PTBQ", "HGZRC"]


def get_top(stacks):
    return (stacks[0][-1] + stacks[1][-1]
            + stacks[2][-1] + stacks[3][-1]
            + stacks[4][-1] + stacks[5][-1]
            + stacks[6][-1] + stacks[7][-1] + stacks[8][-1])


nline = 1
for line in f.readlines():
    if nline != 11:
        nline += 1
        continue
    line = line.replace("move ", "").replace("from ", "").replace("to ", "").strip("\n").split(" ")
    for i in range(0, int(line[0])):
        stacks[int(line[2]) - 1] = stacks[int(line[2]) - 1] + stacks[int(line[1]) - 1][-1]
        stacks[int(line[1]) - 1] = stacks[int(line[1]) - 1][0:-1]
    stacks2[int(line[2]) - 1] = stacks2[int(line[2]) - 1] + stacks2[int(line[1]) - 1][-(int(line[0])):]
    stacks2[int(line[1]) - 1] = stacks2[int(line[1]) - 1][0:-(int(line[0]))]

top = get_top(stacks)
top2 = get_top(stacks2)

print("part one: " + top)
print("part two: " + top2)
f.close()
