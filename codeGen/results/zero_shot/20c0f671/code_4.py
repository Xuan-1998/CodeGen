import sys

# Read input from stdin
n = int(sys.stdin.readline())
books = []
for i in range(n):
    t, h = map(int, sys.stdin.readline().split())
    books.append((t, h))

# Sort books by height in descending order
books.sort(key=lambda x: x[1], reverse=True)

# Initialize the minimum height and the current shelf
min_height = 0
current_shelf = [0, 0]  # [thickness, height]

for book in books:
    if book[0] + current_shelf[0] <= current_shelf[1]:
        # Book fits on the current shelf
        current_shelf[0] += book[0]
        min_height = max(min_height, current_shelf[1])
    else:
        # Start a new shelf
        current_shelf = [book[0], book[1]]
        min_height = max(min_height, current_shelf[1])

print(min_height)
