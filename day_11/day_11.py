f = open("input.txt", "r")
monkeys = [[[], "", "", 0, 0, 0, 0] for i in range(8)]
for line in f.readlines():
    if line == "\n":
        continue
    line = line.replace(":", "").replace(",", "").split()
    if line[0] == "Monkey":
        monkey_id = int(line[1])
    elif line[0] == "Starting":
        line.pop(0)
        line.pop(0)
        for i in line:
            monkeys[monkey_id][0].append(int(i))
    elif line[0] == "Operation":
        if line[4] == "+":
            monkeys[monkey_id][1] = "plus"
        else:
            monkeys[monkey_id][1] = "times"
        if line[5] == "old":
            monkeys[monkey_id][2] = "old"
        else:
            monkeys[monkey_id][2] = int(line[5])
    elif line[0] == "Test":
        monkeys[monkey_id][3] = int(line[3])
    elif line[1] == "true":
        monkeys[monkey_id][4] = int(line[5])
    elif line[1] == "false":
        monkeys[monkey_id][5] = int(line[5])
print(monkeys)

mod = 1
for i in range(8):
    mod *= monkeys[i][3]
print(mod)
for i in range(0, 10000):
    for monkey in monkeys:
        for item in monkey[0]:
            monkey[6] += 1
            if monkey[1] == "plus":
                if monkey[2] == "old":
                    item += item
                else:
                    item += monkey[2]
            else:
                if monkey[2] == "old":
                    item *= item
                else:
                    item *= monkey[2]
            #item = item // 3
            item = item % mod
            if item % monkey[3] == 0:
                monkeys[monkey[4]][0].append(item)
            else:
                monkeys[monkey[5]][0].append(item)
        monkey[0] = []

print(monkeys[0][6])
print(monkeys[1][6])
print(monkeys[2][6])
print(monkeys[3][6])

business = []
for monkey in monkeys:
    business.append(monkey[6])
business.sort()
print(business)
print("result: " + str(business[-1] * business[-2]))

f.close()
