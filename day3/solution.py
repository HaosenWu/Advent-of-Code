with open("data.txt", "r") as f:
    lines = f.read().splitlines()
    # print(lines)

sum = 0

for banks in lines:
    first_digit = 0
    second_digit = 0
    index = 0

    for i in range(len(banks) - 1):
        if int(banks[i]) > first_digit:
            first_digit = int(banks[i])
            index = i

    for val in banks[index + 1 : len(banks)]:
        if int(val) > second_digit:
            second_digit = int(val)

    first_digit *= 10
    sum += first_digit + second_digit

print(sum)

        