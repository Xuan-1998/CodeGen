import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

if n < 3:
    print("NO")
elif sum(moods) <= n // 2:
    print("YES")
else:
    print("NO")
