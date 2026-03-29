n, q = map(int, input().split())
sign = input()
dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)

for i in range(n):
    if sign[i] == '+':
        dp1[i+1] += 1
        dp2[i] -= 1
    else:
        dp1[i+1] -= 1
        dp2[i] += 1

for _ in range(q):
    l, r = map(int, input().split())
    print(dp1[r] - dp1[l-1] + dp2[l-1])
