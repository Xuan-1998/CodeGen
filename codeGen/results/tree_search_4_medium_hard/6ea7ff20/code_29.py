def mergeable(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    def merge(i, j):
        if i == 0 and j == 0:
            return p[:i+j] == []
        if i > 0 and j > 0:
            if p[i+j-1] not in p[:i-1] + p[:j-1]:
                return merge(i-1, j) or merge(i, j-1)
        return False

    for i in range(n + 1):
        for j in range(n + 1):
            dp[i][j] = merge(i, j)

    return "YES" if p[:n] not in [p[:i]] * (n + 1) and p[n:] not in [p[:i]] * (n + 1) else "NO"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        print("YES" if mergeable(p) else "NO")


if __name__ == "__main__":
    main()
