def min_height_of_bookcase():
    n = int(input())  # number of books
    shelves = []
    for _ in range(n):
        thickness, height = map(int, input().split())
        shelf_index = -1
        for i, shelf in enumerate(shelves):
            if sum(book[0] for book in shelf) + thickness <= W:
                shelf.append((thickness, height))
                shelf_index = i
                break
        if shelf_index == -1:  # no empty shelf found, create a new one
            shelves.append([(thickness, height)])
    max_height = 0
    for shelf in shelves:
        max_height = max(max_height, max(book[1] for book in shelf))
    return max_height

W = int(input("Enter the maximum width of each shelf: "))
print(min_height_of_bookcase())
