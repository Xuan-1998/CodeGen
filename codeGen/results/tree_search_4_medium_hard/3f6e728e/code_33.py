import sys

# Read input from stdin
N, M, C = map(int, input().split())
upper_radii = list(map(int, input().split()))
lower_radii = list(map(int, input().split()))

# Initialize memoization dictionary
dp = [[0] * (M+1) for _ in range(C+1)]

def find_lower_hemisphere(r):
    # Your implementation here! For now, let's assume it returns the correct count
    return ...

for i in range(1, C+1):
    for j in range(M+1):
        if upper_radii[i-1] <= i:
            dp[i][j] = sum(dp[k][max(0, j-m)] for k in range(C+1) if k <= i and find_lower_hemisphere(k) >= m)
        else:
            dp[i][j] = 0

print(*dp[C], sep=' ')
