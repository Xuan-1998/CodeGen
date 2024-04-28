def can_sum_subset(n, m):
    dp = [[False for _ in range(m)] for _ in range(n+1)]
    
    # Base case: If there are no elements and the sum is 0, return True.
    dp[0][0] = True
    
    for i in range(1, n+1):
        for j in range(m):
            if dp[i-1][j]:
                # If the current element is less than or equal to m, add it to the subset.
                if j + 1 <= m:
                    dp[i][j+1] = True
            elif dp[i-1][j % m]:
                # If the current element plus the previous sum is divisible by m, add it to the subset.
                dp[i][j] = True
    
    return dp[n][m-1]

# Example usage:
n = int(input("Enter the number of elements: "))
m = int(input("Enter the value: "))

if can_sum_subset(n, m):
    print(1)
else:
    print(0)
