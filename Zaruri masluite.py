n = int(input())

trows = {}

for i in range(n):
    key = input()
    if key in trows:
        trows[key] += 1
    else:
        trows[key] = 1

if max(trows.values()) - min(trows.values()) > n / 10 or len(trows) == 1:
    print(1)
else:
    print(0)
