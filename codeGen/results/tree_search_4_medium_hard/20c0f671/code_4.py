import sys

def min_height_of_bookcase():
    # Read input from standard input
    n, max_width = map(int, input().split())
    books = []
    for _ in range(n):
        t, h = map(int, input().split())
        books.append((t, h))

    dp = {}
    def dfs(i, w):
        if (i, w) in dp:
            return dp[(i, w)]
        if i == 0:
            return 0
        min_height = sys.maxsize
        for j in range(len(books)):
            if books[j][0] <= w:
                min_height = min(min_height, max(dfs(i-1, w-books[j][0]), books[j][1]))
        dp[(i, w)] = min_height
        return min_height

    print(dfs(n, max_width))

if __name__ == "__main__":
    min_height_of_bookcase()
