import sys
from collections import defaultdict, deque

# Read input
books = []
for _ in range(int(sys.stdin.readline())):
    thickness, height = map(int, sys.stdin.readline().split())
    books.append((thickness, height))

shelf_width = int(sys.stdin.readline())

# Sort the books by their heights in descending order
books.sort(key=lambda x: x[1], reverse=True)

# Initialize a queue for BFS
queue = deque([(0, 0)])  # (height, shelf_index)
heights = defaultdict(int)  # dictionary to store the minimum height of each shelf

while queue:
    current_height, shelf_index = queue.popleft()
    
    if shelf_index not in heights or heights[shelf_index] > current_height:
        heights[shelf_index] = current_height
        
    for book_index, (thickness, _) in enumerate(books):
        if shelf_width >= thickness and shelf_index < len(heights) and heights[shelf_index] + _ == current_height:
            queue.append((_ + _, shelf_index))
            break

# The minimum possible height of the bookcase
min_height = max(heights.values())

print(min_height)
