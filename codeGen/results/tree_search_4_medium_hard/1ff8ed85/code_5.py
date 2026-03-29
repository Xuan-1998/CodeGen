code = """
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    dp = [[0] * (max(b) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for prev_val in range(1, b[i - 1] + 1):
            total = b[i - 1] - prev_val
            if total in b[:i]:
                dp[i][prev_val] = 1
    
    for i in range(n + 1):
        for j in range(max(b) + 1):
            if dp[i][j] == 0:
                continue
            for k in range(j, max(b) + 1):
                total = sum(b[:k])
                if total in b and i - 1 > 0 and dp[i - 1][total]:
                    print("YES")
                    sys.exit(0)
    
    print("NO")
"""

print(code)
