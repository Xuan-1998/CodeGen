n = int(input())
dp = {(0, 0): True}
for i in range(1, n+1):
    for k in range(n+1):
        if dp.get((i-1, k), False) and (k >= a[i-1]):
            dp[(i, k)] = True
        else:
            dp[(i, k)] = False
answer = False
for k in range(n+1):
    if dp.get((n, k), False):
        answer = True
        break
if answer:
    print("YES")
else:
    print("NO")
