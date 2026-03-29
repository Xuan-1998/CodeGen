code
import sys

n = int(sys.stdin.readline())
moods = list(map(int, sys.stdin.readline().split()))

if n < 3 or n > 105:
    print("NO")
elif sum(moods) != n // 2 * (1 if moods[0] == 1 else 0):
    print("NO")
else:
    print("YES" if len(set(moods)) <= n // 2 + (n % 2 == 1) else "NO")
