import heapq
from collections import defaultdict

def min_height(books, shelf_width):
    # Sort books by height in descending order
    books.sort(key=lambda x: x[1], reverse=True)
    
    # Create a priority queue to hold the shelves and their heights
    shelves = []
    for book in books:
        heapq.heappush(shelves, (book[1], 0))  # Start each shelf with height 0
    
    # Initialize the minimum height of the bookcase
    min_height = 0
    
    # Place each book on a shelf and update the minimum height
    while shelves:
        shelf_height, _ = heapq.heappop(shelves)
        if sum(books[i][0] for i in range(len(books)) if books[i][1] <= shelf_height) <= shelf_width:
            min_height += shelf_height
        else:
            break
    
    return min_height

# Read input from standard input
n = int(input())
books = []
for _ in range(n):
    thickness, height = map(int, input().split())
    books.append((thickness, height))

shelf_width = int(input())

print(min_height(books, shelf_width))
