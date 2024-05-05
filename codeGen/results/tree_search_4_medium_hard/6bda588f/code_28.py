def f(a, s):
    if not a:  # base case: no more numbers left
        return 0

    n = len(a)
    if s in dp:
        return dp[s]

    res1 = float('inf')
    for i in range(n):
        x = a[i]
        y = x - s
        if (x > s and y > s) or (x <= s and y <= s):  # check the condition
            res2 = f(a[1:], s + (y if x > s else 0))
            dp[s] = min(res1, res2)
            res1 = dp[s]
    return res1

def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        print(f(a, 0))

if __name__ == "__main__":
    dp = {}
    solve()
