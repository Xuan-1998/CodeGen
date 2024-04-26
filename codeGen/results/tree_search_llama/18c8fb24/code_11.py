T = int(input())
for _ in range(T):
    N, x, k = map(int, input().split())
    if (N + 1) % k == 0:
        print("YES")
    else:
        print("NO")
