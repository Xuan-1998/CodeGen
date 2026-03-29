import sys

def merge(a, b):
    result = []
    while a or b:
        if not a and b:
            return result + b
        elif a and not b:
            return result + a
        else:
            if a[0] < b[0]:
                result.append(a.pop(0))
            else:
                result.append(b.pop(0))
    return result

def solve(p):
    n = len(p) // 2
    dp = [[False] * (n+1) for _ in range(len(p)+1)]

    dp[0][j] = True for all j
    for i in range(1, len(p)):
        for j in range(1, min(i+1, n)+1):
            if p[i-1] < p[i-1-j]:
                dp[i][j] = dp[i-1][j]
            elif p[i-1] > p[i-1-j]:
                dp[i][j] = dp[i-1][min(j,j)]
            else:
                dp[i][j] = False

    result = [i for i in range(n+1) if dp[len(p)][i]]
    return "YES" if result else "NO"

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        p = list(map(int, sys.stdin.readline().split()))
        print(solve(p))

if __name__ == "__main__":
    main()
