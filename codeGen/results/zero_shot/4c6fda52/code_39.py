import sys

def min_changes(s, k):
    n = len(s)
    dp = [[False] * (k + 1) for _ in range(n - k + 2)]

    for i in range(1, n - k + 1):
        for j in range(k):
            if s[i-1] == 'R' and s[i+j] == 'G':
                dp[i][j] = True
            elif s[i-1] == 'G' and s[i+j] == 'B':
                dp[i][j] = True
            elif s[i-1] == 'B' and s[i+j] == 'R':
                dp[i][j] = True

    min_changes = 0
    for i in range(n - k + 2):
        if not dp[i][k-1]:
            min_changes += 1

    return min_changes

def main():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        s = input()
        print(min_changes(s, k))

if __name__ == '__main__':
    main()
