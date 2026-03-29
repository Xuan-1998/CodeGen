books = []
shelf_width = 0

while True:
    book_info = input().split()
    if not book_info: break
    thickness, height = map(int, book_info[:2])
    books.append((thickness, height))
    shelf_width = int(book_info[2])

books.sort(key=lambda x: x[1], reverse=True)

shelf_heights = [0]
for book in books:
    for i, shelf_height in enumerate(shelf_heights):
        if book[0] <= shelf_width:
            shelf_heights[i] += book[1]
            break
    else:
        shelf_heights.append(book[1])

print(max(shelf_heights))

