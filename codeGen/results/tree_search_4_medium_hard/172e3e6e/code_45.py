import sys
from collections import defaultdict

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (n + 1)
    count = defaultdict(int)

    for i in range(2, n + 1):
        if dp[i - 1] == 1 and i % arr[i - 1]:
            dp[i], count[i] = 0, 0
        elif dp[i - 1] == 1:
            dp[i], count[i] = 1, count[i - 1]
        else:
            dp[i], count[i] = 0, 0

    result = sum(count.values()) % (10**9 + 7)
    print(result)

if __name__ == "__main__":
    solve()
