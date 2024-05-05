import sys

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    return [b[0]] + merge(a, b[1:])

def can_split(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(len(p) + 1)]
    for i in range(len(p)):
        for j in range(min(i + 1, n) + 1):
            if not p[:i]:
                dp[i][j] = True
            elif not p[i:]:
                dp[i][j] = (p[:i] != p[i:])
            else:
                a = p[:i]
                b = p[i:]
                if a[0] < b[0]:
                    dp[i][j] = a[1:] == b and dp[i - 1][j - 1]
                else:
                    dp[i][j] = a == b[:-1] and dp[i - 1][j]
    return dp[-1][-1]

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        p = list(map(int, sys.stdin.readline().split()))
        if can_split(p):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
