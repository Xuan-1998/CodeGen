import heapq

books = []  # list of (thickness, height) pairs
shelf_width = int(input())  # maximum width of each shelf

# read in all book information
for _ in range(int(input())):
    thickness, height = map(int, input().split())
    books.append((height, -thickness))  # use negative thickness for sorting

books.sort()  # sort by decreasing height and then increasing thickness

shelf_heights = [0]  # initialize with a single shelf
total_height = 0

for book in books:
    while shelf_heights[-1] + book[0] > shelf_width:  # if this book doesn't fit on the last shelf
        shelf_heights.pop()  # remove the last shelf
        total_height -= shelf_heights[-1]  # update total height
    shelf_heights[-1] += book[0]  # place this book on the current shelf
    total_height = max(total_height, shelf_heights[-1])  # update total height

print(total_height)
