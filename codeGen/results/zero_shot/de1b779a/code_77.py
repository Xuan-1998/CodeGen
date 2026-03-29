code block starts here

n, m, c0, d0 = map(int, input().split())
profits = [0] * (m + 1)

for i in range(m):
    ai, bi, ci, di = map(int, input().split())
    if n >= ci and bi <= ai:
        profits[i + 1] = max(profits[i], d0 + di)
    else:
        profits[i + 1] = profits[i]

print(max(profits))
