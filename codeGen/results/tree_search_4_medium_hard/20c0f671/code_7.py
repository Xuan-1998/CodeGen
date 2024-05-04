import sys

def min_height_of_bookcase(books, max_shelf_width):
    n = len(books)
    dp = [[0] * (max_shelf_width + 1) for _ in range(n + 1)]
    memo = {}

    for i in range(1, n + 1):
        for w in range(1, max_shelf_width + 1):
            if books[i-1][0] <= w:  # book fits on current shelf
                dp[i][w] = min(dp[i-1][w], dp[i-1][w-books[i-1][0]] + books[i-1][1])
            else:  # need to start a new shelf
                dp[i][w] = dp[i-1][w]

    return dp[n][max_shelf_width]

def main():
    n = int(input())  # number of books
    max_shelf_width = int(input())
    books = []
    for _ in range(n):
        thickness, height = map(int, input().split())
        books.append((thickness, height))

    min_height = min_height_of_bookcase(books, max_shelf_width)
    print(min_height)

if __name__ == "__main__":
    main()
