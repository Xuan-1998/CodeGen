import sys

def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def solve(n, p):
    dp = [[False for _ in range(n+1)] for _ in range(2*n+1)]
    for i in range(2*n+1):
        if i < n:
            if sorted(p[:i]) == list(range(i)):
                for s in range(n+1):
                    dp[i][s] = True
                break
    for i in range(2*n, -1, -1):
        for s in range(n+1):
            if not dp[i][s]:
                continue
            t = (i-1) // 2
            if i % 2 == 0:
                for j in range(s+1, n+1):
                    if dp[t][j]:
                        dp[i][s] = True
                        break
            else:
                for j in range(n-j):
                    if not dp[t][j]:
                        continue
                    dp[i][s] = True
                    break
    return "YES" if any(dp[2*n-1][s]) else "NO"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print(solve(n, p))

if __name__ == "__main__":
    main()
