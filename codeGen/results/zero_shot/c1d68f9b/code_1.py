import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if abs((moods[i] - moods[(i+1)%n]) % 2) == 1:
        print("NO")
        sys.exit()

print("YES")
