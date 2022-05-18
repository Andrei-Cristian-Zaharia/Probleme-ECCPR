import collections

n = int(input())
numbers = list(map(int, input().split()))

pair_of_numbers = {}

def single_numbers():
    count = 0
    even = -1

    for key in pair_of_numbers.keys():
        if pair_of_numbers[key] % 2 == 1:
            count += 1
            even = key

    return count, even

def check_palindrom():
    count, even = single_numbers()
    if count > 1:
        return False, even

    if len(numbers) % 2 == 0:
        if count > 0:
            return False, even
    else:
        if count != 1:
            return False, even
    return True, even

def create_dict(pair_of_numbers):
    for num in numbers:
        if num in pair_of_numbers.keys():
            continue
        else:
            pair_of_numbers[num] = numbers.count(num)

create_dict(pair_of_numbers=pair_of_numbers)

condition, even = check_palindrom()

if condition == True:
    ordered_dict = collections.OrderedDict(sorted(pair_of_numbers.items(), reverse=True))
    aux = ''

    for key in ordered_dict.keys():
        if key == even and ordered_dict[key] % 2 == 1:
            ordered_dict[key] -= 1
            aux = aux.ljust(int(ordered_dict[key] / 2) + len(aux), str(key))
        elif key == even and ordered_dict[key] % 2 == 0:
            continue
        else:
            aux = aux.ljust(int(ordered_dict[key] / 2) + len(aux), str(key))

    ordered_dict = collections.OrderedDict(sorted(pair_of_numbers.items(), reverse=False))

    if even >= 0:
        aux = str(aux) + str(even)

    for key in ordered_dict.keys():
        if key == even and ordered_dict[key] % 2 == 1:
            ordered_dict[key] -= 1
            aux = aux.ljust(int(ordered_dict[key] / 2) + len(aux), str(key))
        elif key == even and ordered_dict[key] % 2 == 0:
            continue
        else:
            aux = aux.ljust(int(ordered_dict[key] / 2) + len(aux), str(key))

    print(aux)
else:
    print(0)
