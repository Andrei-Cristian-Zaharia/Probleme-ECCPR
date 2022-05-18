n = int(input())
loturi_utile = 0
nr_max = 0

for i in range(n):
    k = int(input())

    if k == 0:
        continue
    elif k > nr_max:
        nr_max = k

    line = list(map(str, input().split()))

    if line.count("C") >= line.count("T") and line.count("R") >= line.count("C") and line.count("C") >= 1 and line.count("R") >=1 and line.count("T") >=1:
        loturi_utile +=1

print(loturi_utile, nr_max)
