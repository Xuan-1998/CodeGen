from sys import stdin

def can_merge(p):
    n = len(p) // 2
    dp = [[False] * (len(p)) for _ in range(len(p))]
    
    # Base case: an empty array and another non-empty array can always be merged
    for i in range(n + 1):
        dp[i][i] = True
        if i < n:
            dp[i][n - 1] = True
    
    for length in range(2, len(p) + 1):
        for i in range(len(p) - length + 1):
            j = i + length - 1
            
            # If the first element is less than the last element
            if p[i] < p[j]:
                dp[i][j] = dp.get((i, j - 1), False)
            else:
                # Try merging everything before the first element with everything after the last element
                dp[i][j] = (dp.get((i - 1, j - 1), False) or not dp.get((i - 1, j), False))
    
    return "YES" if any(dp[i][-1] for i in range(len(p))) else "NO"


# Read the input
n_cases = int(stdin.readline())
for _ in range(n_cases):
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))
    
    print(can_merge(p))
