def solve():
    n, t = map(int, input().split())
    h = list(map(int, input().split()))
    k = list(map(int, input().split()))

    dp = {}

    def dp_func(t):
        if t >= len(k):
            return 0
        if (t, len(k)) in dp:
            return dp[(t, len(k))]
        res = float('inf')
        for i in range(len(k)):
            if k[i] <= t:
                break
            res = min(res, dp_func(k[i]-1) + (k[i]-len(k))%2)
        dp[(t, len(k))] = res
        return res

    print(dp_func(t))

if __name__ == "__main__":
    solve()
