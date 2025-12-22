# read the file
with open("data.txt", "r") as f:
    lines = f.read().splitlines()


cur_dial = 50
zeros = 0

# value based loop
for line in lines:
    dir = line[0]
    dis = int(line[1:])
    old_cur_dial = cur_dial

    if dir == "L":
        cur_dial -= dis
        if cur_dial < 0:
            cur_dial %= 100 
    elif dir == "R":
        cur_dial += dis
        if cur_dial > 99:
            cur_dial %= 100

    if cur_dial == 0:
        print("[DEBUG]: line is ", line, ", dir is ", dir, " dis is ", dis, "old cur_dial was ", old_cur_dial, " new cur_dial is ", cur_dial)
        zeros += 1

print(zeros) 
        

    

