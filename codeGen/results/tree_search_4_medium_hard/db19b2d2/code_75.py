import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    cum_sum = [0] * (m + 1)
    for i in range(m):
        cum_sum[i + 1] = cum_sum[i] + s[i]
    
    total_players = n // m
    if h < m:
        total_players += min(n % m, len(s) - h)
    
    left, right = cum_sum[h], cum_sum[m]
    while right - left > sys.float_info.epsilon:
        mid = (left + right) / 2
        if mid >= total_players:
            right = mid
        else:
            left = mid
    
    ans = max(0, 1 - left / cum_sum[m])
    print(ans)

solve()
