from collections import defaultdict

def min_changes():
    dp = defaultdict(int)
    k = int(input())
    while True:
        n = int(input())
        s = input().strip()
        i = j = 0
        changes = 0
        for p in range(n):
            if p < k:
                j = min(p+k, n)
                changes += dp[p][k-1][s[p-j+1+p-k]]
            else:
                j = n
            for q in range(i, j):
                if s[q] != 'RGB'[q%3]:
                    changes += 1
                i += 1
        print(changes)

min_changes()
