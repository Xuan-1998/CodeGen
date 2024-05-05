t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    if len(b) != n:
        print("NO")
        continue
    
    a = [0] * (n*2 - 1)
    for i in range(n):
        while a[i*2] < b[i]:
            a[i*2+1] += 1
            i -= 1
            if i < 0:
                print("NO")
                break
        else:
            a[i*2+1] = b[i]
    
    print("YES" if all(a[i] == b[j] for i, j in enumerate(range(n))) else "NO")
