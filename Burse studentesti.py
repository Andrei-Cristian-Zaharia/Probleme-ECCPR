import operator

m, n, p = map(int , input().split())

students = {}

def read():
    for i in range(m):
        nume_student = input()
        note = list(map(int, input().split()))

        if all(i >= 5 for i in note):
            students[nume_student] = round(sum(note) / len(note), 2)

def get_merit():
    count = 0

    for i in range(0, p, 1):
        if i < len(students_sorted):
            if students_sorted[i][1] >= 8:
                count += 1
    print(count)

read()
students_sorted = sorted(students.items(), key=operator.itemgetter(1), reverse=True)
best_Student = students_sorted[0]
del students_sorted[0]
get_merit()

print(best_Student[0], F'{best_Student[1]:.2f}')
