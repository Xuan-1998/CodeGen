T = int(input())
for _ in range(T):
    N, x, k = map(int, input().split())
    if (x % k) == 0:
        print("YES")
    else:
        print("NO")
