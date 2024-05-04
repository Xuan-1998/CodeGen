import sys

def solve():
    n, w_shelf_width = map(int, input().split())
    dp = [[0] * (w_shelf_width + 1) for _ in range(n + 1)]
    books = []
    
    # read the books and their sizes
    for _ in range(n):
        thickness, height = map(int, input().split())
        books.append((thickness, height))
        
    # fill up the dp table
    for i in range(1, n + 1):
        for w in range(w_shelf_width, -1, -1):
            if w < books[i-1][0]:
                continue
            
            dp[i][w] = max(dp[i-1][w], dp[i-1][min(w, books[i-1][0])] + books[i-1][1])
    
    # print the minimum possible height of the bookcase
    print(max(dp[n]))

if __name__ == "__main__":
    solve()
