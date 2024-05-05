import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

# Sort the array
m.sort()

ways = 0
for i in range(len(m)):
    ways += (m[i] - m[0]) * (len(m) - i - 1)

print(ways % (10**9 + 7))
