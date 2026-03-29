def dp(i, k):
    if i == n:
        return a_n * (k // (a_n - s))
    if i > 2:
        res = float('inf')
        for x in range(min(k + 1, a_i), min(a_i, k // (a_i - s)) + 1):
            y = a_i - x
            if (x - s) * (y - s) >= 0:
                res = min(res, dp(i-1, k-a_i+s)+a_i*x-s)
        return res
    elif i == 2:
        res = float('inf')
        for y in range(min(a_2, k // (a_2 - s)) + 1):
            x = a_2 - y
            if (x - s) * (y - s) >= 0:
                return min(res, dp(1, k-a_2+s)+a_2*x-s)
    else:
        return float('inf')

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min([dp(1, k) for k in range(s+1, sum(a)-s)]))
