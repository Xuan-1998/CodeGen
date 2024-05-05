from collections import defaultdict

def solve():
    n = int(input())
    s = input()

    dp = defaultdict(int)
    dp[0] = 0

    for i in range(1, n+1):
        c = 0
        for j in range(max(0, i-k), i):
            if s[j] != 'RGB'[j % 3]:
                c += 1
        dp[i] = min(dp.get(i-1, float('inf')), c) if i >= k else 0

    print(dp[n-1])

if __name__ == "__main__":
    solve()
