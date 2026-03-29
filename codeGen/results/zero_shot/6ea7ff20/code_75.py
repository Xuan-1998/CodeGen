n = int(input())
p = list(map(int, input().split()))
p.sort()

if (p[0] == p[n-1]):
    print("YES")
else:
    diff = 1
    for i in range(1, n):
        if abs(p[i] - p[i-1]) > diff:
            print("YES")
            break
        elif p[i] == p[i-1]:
            if (p[0] != p[n-1]):
                print("NO")
                break
    else:
        print("NO")
