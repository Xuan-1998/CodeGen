t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    for a in [[1] + [x+1 for x in b] + [2]]:
        if can_compress(a, b):
            print("YES")
            break
    else:
        print("NO")
