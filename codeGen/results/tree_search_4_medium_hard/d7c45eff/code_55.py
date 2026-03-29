from collections import defaultdict

def smallest_string(n, k):
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    
    # Initialize base cases
    for i in range(k + 1):
        dp[0][i] = True
    
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = True
            elif j < i:
                dp[i][j] = dp[i - 1][j]
            else:
                # Check if deleting the last character or duplicating the string works
                if dp[i - 1][j - 1]:
                    dp[i][j] = True
    
    # Find the smallest string of length k
    for i in range(n, -1, -1):
        if dp[i][k]:
            break
    
    # Construct the smallest string of length k
    result = ''
    for j in range(k, 0, -1):
        if dp[i][j] and not dp[i - 1][j - 1]:
            result += 'c'
        elif dp[i][j]:
            i -= 1
    
    return result

n, k = map(int, input().split())
print(smallest_string(n, k))
