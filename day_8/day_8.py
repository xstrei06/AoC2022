f = open("input.txt", "r")
grid = []
i = 0
count = 0
visible = 0
maximum = 0
for line in f.readlines():
    line = list(line.strip('\n'))
    grid.append(line)
    i += 1
index_row = 0
for item in grid:
    index_column = 0
    for itm in grid[index_row]:
        left = 0
        right = 0
        up = 0
        down = 0
        for it in reversed(grid[0:index_row]):
            up += 1
            if it[index_column] >= grid[index_row][index_column]:
                visible += 1
                break

        for it in grid[index_row+1:]:
            down += 1
            if it[index_column] >= grid[index_row][index_column]:
                visible += 1
                break

        for it in reversed(grid[index_row][0: index_column]):
            left += 1
            if it >= grid[index_row][index_column]:
                visible += 1
                break

        for it in grid[index_row][index_column+1:]:
            right += 1
            if it >= grid[index_row][index_column]:
                visible += 1
                break
        if maximum < (up*down*left*right):
            maximum = up*down*left*right

        if visible < 4:
            count += 1
        visible = 0
        index_column += 1
    index_row += 1
print("part one: " + str(count))
print("part two: " + str(maximum))
f.close()
