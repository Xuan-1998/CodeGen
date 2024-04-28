v1, v2 = map(int, input().split())
t, dv = map(int, input().split())

ans = 0
for i in range(t):
    if i == 0:
        ans += (v2 - v1) * dv
    elif i == t-1:
        ans += (v2 - v1) * dv
    else:
        ans += (v2 - v1) + 2*dv
print(ans)
