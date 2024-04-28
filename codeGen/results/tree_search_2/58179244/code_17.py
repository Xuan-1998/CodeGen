from collections import defaultdict

def solve():
    n = int(input())
    s = input()

    memo = defaultdict(lambda: defaultdict(bool))

    def dp(i, p):
        if p < 0:
            return False
        if i == 0:
            return p == 0
        if memo[i][p]:
            return memo[i][p]
        
        if s[i-1] in 'RGB':
            res = dp(i-1, p) or (dp(i-1, p-1) and (s[i-2] != s[i-1]))
        else:
            res = dp(i-1, p)
        
        memo[i][p] = res
        return res

    r = 0
    t = list(s)

    for i in range(n):
        if not dp(i+1, r+1):
            break
        r += 1

    print(r)
    print(''.join(t))

if __name__ == "__main__":
    solve()
