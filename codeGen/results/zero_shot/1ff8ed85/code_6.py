def check_sequence(b):
    n = len(b)
    for i in range(n-1):
        for j in range(i+1, n):
            s = b[i] + b[j]
            d = abs(b[i] - b[j])
            if s not in b and d not in b:
                return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    if check_sequence(b):
        print("YES")
    else:
        print("NO")
