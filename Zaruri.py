n = int(input())
suma = 0

for i in range(n):
    zaruri = list(map(int, input().split()))
    suma_provizorie = abs(sum(zaruri) - 21)
    suma += suma_provizorie

print(suma)
