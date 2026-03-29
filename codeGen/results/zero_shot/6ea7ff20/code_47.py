n = int(input())
p = list(map(int, input().split()))
p.sort()
if p[::2] != p[1::2]:
    print("NO")
else:
    print("YES")
