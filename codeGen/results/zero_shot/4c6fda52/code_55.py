import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    s = list(sys.stdin.readline().strip())

    min_changes = 0
    r_count = 0
    for i in range(n):
        if s[i] == 'R':
            r_count += 1
        elif i >= k:
            if s[i-k] == 'R':
                r_count -= 1

        if r_count % 2 != 0 and i >= k-1:
            min_changes += 1

    print(min_changes)
