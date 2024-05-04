books.sort(key=lambda x: x[1], reverse=True)

shelves = []
current_height = 0

for book in books:
    for i, shelf in enumerate(shelves):
        if sum(b[0] for b in shelf) + book[0] <= shelf_width:
            shelf.append(book)
            break
    else:
        shelves.append([book])
        current_height += book[1]

total_height = current_height
print(total_height)
