def solve(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        if i < k:
            dp[i][k] = dp[i][k - 1]
        else:
            last_char = s[n - i]
            smaller_str = dp[i - 1][k - 1]
            if lexicographically_smaller(last_char, smaller_str):
                dp[i][k] = last_char
            else:
                dp[i][k] = smaller_str
    
    return dp[n][k]

def lexicographically_smaller(a, b):
    # implementation of the lexicographically smaller function
    pass

n, k = map(int, input().split())
s = input()
print(solve(n, k))
