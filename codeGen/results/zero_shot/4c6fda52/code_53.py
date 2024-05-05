def min_changes(s, k):
    n = len(s)
    changes = 0
    for i in range(0, n, k):
        chunk = s[i:i+k]
        if chunk != "RGB" * (k // 3):
            changes += 1
    return changes

while True:
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))
