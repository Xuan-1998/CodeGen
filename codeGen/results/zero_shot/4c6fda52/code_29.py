def min_changes():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        changes = 0
        for i in range(k-1, n):
            if (s[i] != 'R' and s[i] != 'B') or ((i-k+2) % 3 == 0 and s[i] != 'G'):
                changes += 1
        print(changes)

min_changes()
