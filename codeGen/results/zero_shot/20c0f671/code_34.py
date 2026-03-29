import sys
from collections import deque

def min_height_of_bookcase():
    # Read input
    n = int(sys.stdin.readline())
    books = []
    for _ in range(n):
        thickness, height = map(int, sys.stdin.readline().split())
        books.append((thickness, height))

    max_width = int(sys.stdin.readline())

    # Sort the books by their heights
    books.sort(key=lambda x: x[1])

    dp = [0] * (max_width + 1)
    for thickness, height in books:
        for i in range(max_width, thickness - 1, -1):
            dp[i] = max(dp[i], dp[i - thickness] + height)

    # Print the answer
    print(dp[max_width])

min_height_of_bookcase()
