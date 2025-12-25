with open("data.txt", "r") as f:
    lines = f.read().splitlines()


mat = []
ls = []

for line in lines:
    for ch in line:
        ls.append(ch)
    mat.append(ls[:]) 
    ls.clear()

cnt = 0
rows = len(mat)
cols = len(mat[0])
res = 0

# iterate throguh every position in the matrix
for i in range(rows):
    for j in range(cols):
        if mat[i][j] != '@':
            continue
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                new_i = i + di
                new_j = j + dj
                if new_i >= 0 and new_i < rows and new_j >= 0 and new_j < cols and mat[new_i][new_j] == '@':
                    cnt += 1
        if cnt < 4:
            res += 1
        cnt = 0

print(res)