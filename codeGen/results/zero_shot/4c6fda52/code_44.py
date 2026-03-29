def min_changes(s, k):
    count = 0
    for i in range(k-1):
        if s[i] == 'R':
            count += 2
        elif s[i] == 'G':
            count += 1
        else:
            count += 2
    return count

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))
