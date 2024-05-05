import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

if n < 3:
    print("NO")
else:
    for i in range(n - 2):
        if (moods[i] + moods[i+1] + moods[i+2]) not in [0, 2]:
            print("NO")
            break
    else:
        print("YES")
