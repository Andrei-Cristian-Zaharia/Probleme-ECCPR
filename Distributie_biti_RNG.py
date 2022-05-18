n = int(input())

biti_2 = {}
R = [0, 0]

def init():
    biti = input()
    split_strings = [biti[index: index + 2] for index in range(0, len(biti), 2)]

    for comb in split_strings:
        if comb not in biti_2:
            biti_2[comb] = 1
        else:
            biti_2[comb] += 1

    R[0] = round(max(biti_2.values()) / min(biti_2.values()), 2)

    if biti.count("0") > biti.count("1"):
        R[1] = round(biti.count("0") / biti.count("1"), 2)
    else:
        R[1] = round(biti.count("1") / biti.count("0"), 2)

init()

print(R[0], R[1])

if R[0] > 1.1 or R[1] > 1.1:
    print("0")
else:
    print("1")
