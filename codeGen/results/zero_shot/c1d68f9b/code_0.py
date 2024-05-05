import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

if sum(moods) >= 3:
    print("YES")
else:
    print("NO")
