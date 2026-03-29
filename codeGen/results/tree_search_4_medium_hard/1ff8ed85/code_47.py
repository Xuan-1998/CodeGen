import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            if any(dp[j] for j in range(i)) and all((b[k]%2) == (b[j]%2) for k in range(j)):
                dp[i] = True
        print('YES' if dp[-1] else 'NO')

if __name__ == "__main__":
    main()
