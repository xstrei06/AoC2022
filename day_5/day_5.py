f = open("input.txt", "r")
stack1 = "T D W Z V P"
stack2 = "L S W V F J D"
stack3 = "Z M L S V T B H"
stack4 = "R S J"
stack5 = "C Z B G F M L W"
stack6 = "Q W V H Z R G B"
stack7 = "V J P C B D N"
stack8 = "P T B Q"
stack9 = "H G Z R C"

stack1 = stack1.split(" ")
stack2 = stack2.split(" ")
stack3 = stack3.split(" ")
stack4 = stack4.split(" ")
stack5 = stack5.split(" ")
stack6 = stack6.split(" ")
stack7 = stack7.split(" ")
stack8 = stack8.split(" ")
stack9 = stack9.split(" ")

nline = 1
for line in f.readlines():
    if nline != 11:
        nline += 1
        continue
    line = line.replace("move ", "").replace("from ", "").replace("to ", "").strip("\n").split(" ")
    print(line)
    i = int(line[0])
    match line[1]:
        case "1":
            first = stack1
        case "2":
            first = stack2
        case "3":
            first = stack3
        case "4":
            first = stack4
        case "5":
            first = stack5
        case "6":
            first = stack6
        case "7":
            first = stack7
        case "8":
            first = stack8
        case "9":
            first = stack9
        case _:
            continue
print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)

f.close()