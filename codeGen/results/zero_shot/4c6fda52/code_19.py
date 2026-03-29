def min_changes(s, k):
    n = len(s)
    if n < k:
        return n - (n % 3)

    changes = 0
    for i in range(k-1):
        c = s[i]
        if c == 'R':
            changes += (2 - (i % 3))
        elif c == 'G':
            changes += (1 - (i % 3))
        else:
            changes += (0 - (i % 3))

    return changes

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))
