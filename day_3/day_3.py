f1 = open("input.txt", "r")
first_half = ""
second_half = ""
sum_errors = 0
sum_badges = 0
nline = 1
for line in f1.readlines():
    line = line.replace("\n", "")
    first_half = line[0:(len(line)//2):]
    second_half = line[len(line)//2::]
    if nline == 1:
        line1 = line
    if nline == 2:
        line2 = line
    if nline == 3:
        line3 = line
        for i in line1:
            if i in line2:
                if i in line3:
                    if i.isupper():
                        sum_badges += (ord(i) - 38)
                        break
                    else:
                        sum_badges += (ord(i) - 96)
                        break
        nline = 0
    for i in first_half:
        if i in second_half:
            if i.isupper():
                sum_errors += (ord(i)-38)
            else:
                sum_errors += (ord(i)-96)
            break
    nline += 1
f1.close()
print("sum_errors: " + str(sum_errors))
print("sum_badges: " + str(sum_badges))
