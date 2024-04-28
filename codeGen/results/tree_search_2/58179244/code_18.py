import sys

def solve():
    n = int(input())
    s = input()

    memo = {}

    def dp(i, p):
        if (i, p) in memo:
            return memo[(i, p)]
        
        if i < 1:
            memo[(i, p)] = False
            return False
        
        if i == 1:
            memo[(i, p)] = True
            return True

        diverse = False
        for j in range(p + 1):
            if (i - 1, j) not in memo and dp(i - 1, j):
                if j < p and s[i - 2] == s[i - 1]:
                    continue
                diverse = True
                break
        
        memo[(i, p)] = diverse
        return diverse

    r = 0
    t = list(s)

    for i in range(n):
        if dp(i + 1, r):
            r += 1
        else:
            break

    print(r)
    print(''.join(t[:r]))
