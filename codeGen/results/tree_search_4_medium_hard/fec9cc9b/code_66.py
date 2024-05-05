import sys

def is_ladder(a, l, r):
    # Initialize variables
    inc_len = 0
    dec_len = 0

    # Iterate through the subsegment from l to r
    for i in range(l-1, r):
        if a[i] < a[i+1]:
            if inc_len > 0:
                return "No"
            inc_len += 1
        elif a[i] > a[i+1]:
            dec_len = max(dec_len, inc_len)
            inc_len = 0

    return "Yes" if inc_len + dec_len == r - l + 1 else "No"


n, m = map(int, input().split())
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(m)]

for l, r in queries:
    print(is_ladder(a[l-1:r], l, r))
