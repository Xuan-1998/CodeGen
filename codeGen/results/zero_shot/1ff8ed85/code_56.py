def check_transform(a, b):
    n = len(b)
    for i in range(n):
        if a[i] < b[i]:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    if all(a <= b[i] - a[i-1] for i in range(1, n)):
        print("YES")
    else:
        print("NO")
