def dp(i, l, r):
    if i == n:  # base case
        return 0

    min_ops = float('inf')
    for val in range(l_i, r_i + 1):
        new_l = max(l, val)
        new_r = min(r, val + (r_i - l_i) // (val - l_i))
        if new_l == l and new_r == r:
            continue
        ops = dp(j, new_l, new_r) + abs(new_l - l_i)  # adjust vertex i's value
        min_ops = min(min_ops, ops)

    return min_ops

n = int(input())
p = list(map(int, input().split()))
l = [int(x) for x in map(str.split, open('input.txt', 'r'))[1:]]
r = [int(x) for x in map(str.split, open('input.txt', 'r'))[2:]]

min_ops = dp(0, 0, 10**9)
print(min_ops)
