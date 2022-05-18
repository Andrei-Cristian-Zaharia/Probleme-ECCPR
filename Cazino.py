n = int(input())

def cazino() -> bool:
    dict = {}

    for i in range(n):
        carte = input()

        if carte not in dict:
            dict[carte] = 1
        else:
            dict[carte] += 1

        if dict[carte] > 2:
            print(carte)
            return False

    return True

if cazino():
    print("JOC OK")
