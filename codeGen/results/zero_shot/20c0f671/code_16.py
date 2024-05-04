import heapq

books = []
shelf_width = None
with open('input.txt', 'r') as f:
    for line in f:
        book_thickness, book_height = map(int, line.split())
        books.append((book_thickness, book_height))
        if shelf_width is None:
            shelf_width = book_thickness

books.sort(key=lambda x: x[1], reverse=True)

current_shelf_height = 0
current_shelf_books = [books[0]]
shelves = [(current_shelf_height, current_shelf_books)]
del books[0]

for book in books:
    if sum([book[0] for book in current_shelf_books]) + book[0] <= shelf_width:
        current_shelf_books.append(book)
    else:
        shelves.append((current_shelf_height, current_shelf_books))
        current_shelf_height = 0
        current_shelf_books = [book]

bookcase_height = sum([shelf[0] for shelf in shelves])
print(bookcase_height)
