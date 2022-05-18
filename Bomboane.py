n = int(input())

money = list(map(int, input().split()))
Andrei = [0, 0] # money and happiness
value = 0

for i in range(n):
    candy = list(map(int, input().split()))

    if candy[0] <= money[i] + Andrei[0]:
        Andrei[0] += money[i] - candy[0]
        Andrei[1] += candy[1]

        if candy[1] >= value:
            value = candy[1]
    else:
        Andrei[0] += money[i]

        if candy[1] >= value:
            Andrei[1] -= candy[1]

print(Andrei[1])
