from sys import stdin, maxsize

def solve():
    n = int(stdin.readline())
    dp = [[False] * (n + 1) for _ in range(maxsize)]
    ans = 0
    for i in range(n+1):
        k = 0
        while i > 0:
            if i & 1: 
                k += 1
            i //= 2
        dp[k][i] = True
    for i in range(1, n + 1):
        ans += int(dp[0][i])
    print(ans)

if __name__ == "__main__":
    solve()
