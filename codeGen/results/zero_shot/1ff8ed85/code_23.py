import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    a = ""
    for bi in b:
        if not a or str(len(a)) + ' ' + str(bi) == a:
            a += str(len(a)) + ' ' + str(bi)
        else:
            print("NO")
            break
    else:
        print("YES")
