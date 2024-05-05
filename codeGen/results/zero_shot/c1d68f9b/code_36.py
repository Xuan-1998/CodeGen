import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

if all(mood == moods[0] for mood in moods):
    print("YES")
else:
    print("NO")
