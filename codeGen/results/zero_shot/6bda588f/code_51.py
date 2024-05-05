t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    min_F_val = float('inf')
    for i in range(s, 2*s+1):
        F_val = min_F(a, i)
        if F_val < min_F_val:
            min_F_val = F_val
    print(min_F_val)
