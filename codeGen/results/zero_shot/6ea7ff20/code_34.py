n = int(input())
p = list(map(int, input().split()))
x1, y1 = None, None
for pi in p:
    if x1 is None:
        x1 = pi
    else:
        y1 = pi
if (x1 and y1) or (not x1 and not y1):
    print("NO")
else:
    print("YES")
