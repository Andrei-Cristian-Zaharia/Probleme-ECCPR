registre = {}

def lconst(dst, val):
    registre[dst] = val

def add(dst, scr0, src1):
    registre[dst] = int(registre[scr0]) + int(registre[src1])

def mul(dst, src0, src1):
    registre[dst] = float(registre[src0]) * float(registre[src1])

def div(dst, src0, src1) -> bool:

    if int(src1) == 0:
        return False
    else:
        registre[dst] = float(registre[src0]) / float(registre[src1])

def print_reg(reg):
    print(int(registre[reg]))

n = int(input())

for i in range(n):
    inst = list(map(str, input().split()))

    if inst[0] == "lconst":
        lconst(dst=inst[1], val=inst[2])
    elif inst[0] == "add":
        add(dst=inst[1], scr0=inst[2], src1=inst[3])
    elif inst[0] == "mul":
        mul(dst=inst[1], src0=inst[2], src1=inst[3])
    elif inst[0] == "div":
        if div(dst=inst[1], src0=inst[2], src1=inst[3]) == False:
            print("Exception: line:" + str(i + 1))
            break
    elif inst[0] == "print":
        print_reg(reg=inst[1])
