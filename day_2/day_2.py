f = open("input.txt", 'r')
score1 = 0
score2 = 0
for line in f.readlines():
    line = line.split(' ')
    line[-1] = line[-1].strip()
    if line[0] == "A":
        match line[1]:
            case "X":
                score1  += (1+3)
                score2 += (3+0)
            case "Y":
                score1  += (2+6)
                score2 += (1+3)
            case "Z":
                score1  += (3+0)
                score2 += (2+6)
            case _:
                continue
    elif line[0] == "B":
        match line[1]:
            case "X":
                score1  += (1+0)
                score2 += (1+0)
            case "Y":
                score1  += (2+3)
                score2 += (2+3)
            case "Z":
                score1  += (3+6)
                score2 += (3+6)
            case _:
                continue
    elif line[0] == "C":
        match line[1]:
            case "X":
                score1 += (1+6)
                score2 += (2+0)
            case "Y":
                score1 += (2+0)
                score2 += (3+3)
            case "Z":
                score1 += (3+3)
                score2 += (1+6)
            case _:
                continue
print(score1)
print(score2)
f.close()
