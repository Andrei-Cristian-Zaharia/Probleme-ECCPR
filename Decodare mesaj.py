N, k = input().split()

max = 0

def algorithm(num):
    new_number = ""
    i = 0

    while i < len(num):
        if i == len(num) - 1:
            break

        if i + 1 < len(num):
            new_number += str(abs(int(num[i]) - int(num[i + 1])))

        i += 1
    return new_number

numbers_list = list(map(str, input().split()))

for i in range(int(N)):
    s = []

    for j in range(int(k)):

        if int(numbers_list[i]) < 9:
            s.append(numbers_list[i])
            break

        if j > 1 and int(s[j - 1]) < 9:
            s.append(s[j - 1])
            continue

        if j == 0:
            s.append(algorithm(num=numbers_list[i]))
        else:
            s.append(algorithm(num=s[j - 1]))

    if sum(list(map(int, s))) > max:
        max = sum(list(map(int, s)))

print(max)


