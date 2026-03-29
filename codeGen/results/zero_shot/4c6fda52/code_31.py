import sys

def min_changes_to_find_substring(s, k):
    n = len(s)
    dp = [[False] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            substring = s[i - j:i]
            if substring == "RGB" * (j // 3):
                dp[i][j] = True

    changes = sum(1 for i in range(n) if not dp[i][k])
    return changes

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()
        print(min_changes_to_find_substring(s, k))

if __name__ == "__main__":
    main()
