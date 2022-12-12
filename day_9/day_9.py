f = open("input.txt", "r")
head = [0, 0]
tail = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited = []
visited2 = []
count = 0
count2 = 0
for line in f.readlines():
    line = line.split()
    match line[0]:
        case "R":
            for i in range(0, int(line[1])):
                head[1] += 1
                if abs(head[1] - tail[0][1]) > 1:
                    tail[0][1] += 1
                    if head[0] != tail[0][0]:
                        tail[0][0] = head[0]
                if tail[0] not in visited:
                    visited.append([tail[0][0], tail[0][1]])
                for j in range(1, 9):
                    if (tail[j-1][1] - tail[j][1]) > 1:
                        tail[j][1] += 1
                        if (tail[j - 1][0] - tail[j][0]) < -1:
                            tail[j][0] -= 1
                        elif (tail[j - 1][0] - tail[j][0]) > 1:
                            tail[j][0] += 1
                        elif tail[j - 1][0] != tail[j][0]:
                            tail[j][0] = tail[j - 1][0]

                    elif (tail[j-1][1] - tail[j][1]) < -1:
                        tail[j][1] -= 1
                        if (tail[j - 1][0] - tail[j][0]) < -1:
                            tail[j][0] -= 1
                        elif (tail[j - 1][0] - tail[j][0]) > 1:
                            tail[j][0] += 1
                        elif tail[j - 1][0] != tail[j][0]:
                            tail[j][0] = tail[j - 1][0]

                    elif (tail[j - 1][0] - tail[j][0]) < -1:
                        tail[j][0] -= 1
                        if (tail[j - 1][1] - tail[j][1]) > 1:
                            tail[j][1] += 1
                        elif (tail[j - 1][1] - tail[j][1]) < -1:
                            tail[j][1] -= 1
                        elif tail[j - 1][1] != tail[j][1]:
                            tail[j][1] = tail[j - 1][1]

                    elif (tail[j - 1][0] - tail[j][0]) > 1:
                        tail[j][0] += 1
                        if (tail[j - 1][1] - tail[j][1]) > 1:
                            tail[j][1] += 1
                        elif (tail[j - 1][1] - tail[j][1]) < -1:
                            tail[j][1] -= 1
                        elif tail[j - 1][1] != tail[j][1]:
                            tail[j][1] = tail[j - 1][1]
                if tail[8] not in visited2:
                    visited2.append([tail[8][0], tail[8][1]])
        case "L":
            for i in range(0, int(line[1])):
                head[1] -= 1
                if abs(head[1] - tail[0][1]) > 1:
                    tail[0][1] -= 1
                    if head[0] != tail[0][0]:
                        tail[0][0] = head[0]
                if tail[0] not in visited:
                    visited.append([tail[0][0], tail[0][1]])
                for j in range(1, 9):
                    if (tail[j - 1][1] - tail[j][1]) > 1:
                        tail[j][1] += 1
                        if (tail[j - 1][0] - tail[j][0]) < -1:
                            tail[j][0] -= 1
                        elif (tail[j - 1][0] - tail[j][0]) > 1:
                            tail[j][0] += 1
                        elif tail[j - 1][0] != tail[j][0]:
                            tail[j][0] = tail[j - 1][0]

                    elif (tail[j - 1][1] - tail[j][1]) < -1:
                        tail[j][1] -= 1
                        if (tail[j - 1][0] - tail[j][0]) < -1:
                            tail[j][0] -= 1
                        elif (tail[j - 1][0] - tail[j][0]) > 1:
                            tail[j][0] += 1
                        elif tail[j - 1][0] != tail[j][0]:
                            tail[j][0] = tail[j - 1][0]

                    elif (tail[j - 1][0] - tail[j][0]) < -1:
                        tail[j][0] -= 1
                        if (tail[j - 1][1] - tail[j][1]) > 1:
                            tail[j][1] += 1
                        elif (tail[j - 1][1] - tail[j][1]) < -1:
                            tail[j][1] -= 1
                        elif tail[j - 1][1] != tail[j][1]:
                            tail[j][1] = tail[j - 1][1]

                    elif (tail[j - 1][0] - tail[j][0]) > 1:
                        tail[j][0] += 1
                        if (tail[j - 1][1] - tail[j][1]) > 1:
                            tail[j][1] += 1
                        elif (tail[j - 1][1] - tail[j][1]) < -1:
                            tail[j][1] -= 1
                        elif tail[j - 1][1] != tail[j][1]:
                            tail[j][1] = tail[j - 1][1]
                if tail[8] not in visited2:
                    visited2.append([tail[8][0], tail[8][1]])
        case "D":
            for i in range(0, int(line[1])):
                head[0] -= 1
                if abs(head[0] - tail[0][0]) > 1:
                    tail[0][0] -= 1
                    if head[1] != tail[0][1]:
                        tail[0][1] = head[1]
                if tail[0] not in visited:
                    visited.append([tail[0][0], tail[0][1]])
                for j in range(1, 9):
                    if (tail[j - 1][1] - tail[j][1]) > 1:
                        tail[j][1] += 1
                        if (tail[j - 1][0] - tail[j][0]) < -1:
                            tail[j][0] -= 1
                        elif (tail[j - 1][0] - tail[j][0]) > 1:
                            tail[j][0] += 1
                        elif tail[j - 1][0] != tail[j][0]:
                            tail[j][0] = tail[j - 1][0]

                    elif (tail[j - 1][1] - tail[j][1]) < -1:
                        tail[j][1] -= 1
                        if (tail[j - 1][0] - tail[j][0]) < -1:
                            tail[j][0] -= 1
                        elif (tail[j - 1][0] - tail[j][0]) > 1:
                            tail[j][0] += 1
                        elif tail[j - 1][0] != tail[j][0]:
                            tail[j][0] = tail[j - 1][0]

                    elif (tail[j - 1][0] - tail[j][0]) < -1:
                        tail[j][0] -= 1
                        if (tail[j - 1][1] - tail[j][1]) > 1:
                            tail[j][1] += 1
                        elif (tail[j - 1][1] - tail[j][1]) < -1:
                            tail[j][1] -= 1
                        elif tail[j - 1][1] != tail[j][1]:
                            tail[j][1] = tail[j - 1][1]

                    elif (tail[j - 1][0] - tail[j][0]) > 1:
                        tail[j][0] += 1
                        if (tail[j - 1][1] - tail[j][1]) > 1:
                            tail[j][1] += 1
                        elif (tail[j - 1][1] - tail[j][1]) < -1:
                            tail[j][1] -= 1
                        elif tail[j - 1][1] != tail[j][1]:
                            tail[j][1] = tail[j - 1][1]

                if tail[8] not in visited2:
                    visited2.append([tail[8][0], tail[8][1]])
        case "U":
            for i in range(0, int(line[1])):
                head[0] += 1
                if abs(head[0] - tail[0][0]) > 1:
                    tail[0][0] += 1
                    if head[1] != tail[0][1]:
                        tail[0][1] = head[1]
                if tail[0] not in visited:
                    visited.append([tail[0][0], tail[0][1]])
                for j in range(1, 9):
                    if (tail[j - 1][1] - tail[j][1]) > 1:
                        tail[j][1] += 1
                        if (tail[j - 1][0] - tail[j][0]) < -1:
                            tail[j][0] -= 1
                        elif (tail[j - 1][0] - tail[j][0]) > 1:
                            tail[j][0] += 1
                        elif tail[j - 1][0] != tail[j][0]:
                            tail[j][0] = tail[j - 1][0]

                    elif (tail[j - 1][1] - tail[j][1]) < -1:
                        tail[j][1] -= 1
                        if (tail[j - 1][0] - tail[j][0]) < -1:
                            tail[j][0] -= 1
                        elif (tail[j - 1][0] - tail[j][0]) > 1:
                            tail[j][0] += 1
                        elif tail[j - 1][0] != tail[j][0]:
                            tail[j][0] = tail[j - 1][0]

                    elif (tail[j - 1][0] - tail[j][0]) < -1:
                        tail[j][0] -= 1
                        if (tail[j - 1][1] - tail[j][1]) > 1:
                            tail[j][1] += 1
                        elif (tail[j - 1][1] - tail[j][1]) < -1:
                            tail[j][1] -= 1
                        elif tail[j - 1][1] != tail[j][1]:
                            tail[j][1] = tail[j - 1][1]

                    elif (tail[j - 1][0] - tail[j][0]) > 1:
                        tail[j][0] += 1
                        if (tail[j - 1][1] - tail[j][1]) > 1:
                            tail[j][1] += 1
                        elif (tail[j - 1][1] - tail[j][1]) < -1:
                            tail[j][1] -= 1
                        elif tail[j - 1][1] != tail[j][1]:
                            tail[j][1] = tail[j - 1][1]

                if tail[8] not in visited2:
                    visited2.append([tail[8][0], tail[8][1]])
        case _:
            continue
for i in visited:
    count += 1
for i in visited2:
    count2 += 1
print("part one: " + str(count))
print("part two: " + str(count2))
f.close()
