n = int(input())
binary = bin(n)[2:]

auxiliar_pos = [0, 0]
auxiliar_max = 0

pos = [0, 0]
max_binary = "0b"
count = 0
max_count = 0
ok = False
aux_pos_0 = 0

for i in range(len(binary)):
    if 1 == int(binary[i]):
        auxiliar_max += 1
        auxiliar_pos[0] = i
    else:
        break

for i in range(len(binary), 0, -1):
    if 1 == int(binary[i - 1]):
        auxiliar_max += 1
        auxiliar_pos[1] = i
    else:
        break

for i in range(len(binary)):
    if 1 == int(binary[i]):
        if ok == False:
            count = 1
            aux_pos_0 = i
            ok = True
        else:
            count += 1
    else:
        ok = False

        if max_count < count:
            max_count = count
            pos[0] = aux_pos_0
            pos[1] = i

if len(binary) > 1:
    if max_count >= auxiliar_max:
        for i in range(max_count): max_binary += "1"

        max_binary += binary[pos[1]:len(binary)]
        max_binary += binary[0:pos[0]]
    else:
        for i in range(auxiliar_max): max_binary += "1"

        max_binary += binary[auxiliar_pos[0] + 1:auxiliar_pos[1] - 1]
else:
    max_binary += "1"

print(int(max_binary, 2))
