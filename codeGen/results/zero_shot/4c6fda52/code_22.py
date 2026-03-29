import sys

def min_changes(s, k):
    # ... (same as above)

n = int(sys.stdin.readline())
for _ in range(n):
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(min_changes(s, k))
