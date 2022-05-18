D, k = map(int, input().split())

books = {}
bookshelf = []

for i in range(k):
    book = list(map(int, input().split()))
    books[book[1]] = book[0]

def check(space):
    for book in books.items():
        if book[0] <= space and book[1] > 0:
            books[book[0]] -= 1
            return True, book[0]

    return False, 0

def add_book(row, space):

    while space > 0:
        ok, value = check(space=space)

        if ok == True:
            row.append(value)
            space -= value
        else:
            break

    return row

while max(books.values()) > 0:
    current_row = []

    current_row = add_book(row=current_row, space=D)
    bookshelf.append(current_row)

print(bookshelf)
