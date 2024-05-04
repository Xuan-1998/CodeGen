def min_height_of_bookcase():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    book_info = []
    for i in range(n):
        book_thickness, book_height = map(int, input().split())
        book_info.append((book_thickness, book_height))
        
    for i in range(1, n + 1):
        thickness, height = book_info[i - 1]
        for j in range(m + 1):
            dp[i][j] = min(dp[i-1][k] + height for k in range(j+1) if k >= thickness)
    
    return min(dp[n])

print(min_height_of_bookcase())
