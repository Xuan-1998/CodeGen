def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [0] * (n + 1)
        memo = {0: 1}
        for i in range(1, n + 1):
            if i not in memo:
                memo[i] = i
            for j in range(i - 1, min(m + 1, i)):
                memo[i] = min(memo[i], memo[i - j] + 1)
        print((memo[n] % (10**9 + 7)))

if __name__ == "__main__":
    solve()
