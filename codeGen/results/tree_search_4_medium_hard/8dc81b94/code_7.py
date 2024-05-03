def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Base case: If all elements are already zero, return "YES"
    if all(x == 0 for x in arr):
        print("YES")
        return
    
    # Initialize the table with -1
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    
    # Fill the table using a bottom-up approach
    for i in range(1, n + 1):
        for j in range(n - 1, -1, -1):
            if arr[i - 1] == 0:
                dp[i][j] = 0
            elif i > 0 and dp[i - 1][j] != -1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j < n - 1 and dp[i][j + 1] != -1:
                dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
    
    # Return "YES" if there's a path that leads to all elements being equal to zero
    if dp[n - 1][n - 1] <= 0:
        print("YES")
    else:
        print("NO")

can_make_zero()
