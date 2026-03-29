import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    cum_sum = 0
    for sign in signs:
        if sign == '+':
            cum_sum += 1
        else:
            cum_sum -= 1

    for _ in range(q):
        l, r = map(int, input().split())
        range_cum_sum = [0] * (r - l + 1)
        for i in range(r - l + 1):
            if signs[l + i] == '+':
                range_cum_sum[i] += 1
            else:
                range_cum_sum[i] -= 1

        min_range_cum_sum = min(range_cum_sum)
        print(min_range_cum_sum)

solve()
